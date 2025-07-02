# modules/render.py
#
# Provides abstractions for more high-level graphics.
# pyopengl was the utilized module.
#
# Note: this little engine was created for small projects (pysand),
# and perfomance won't look good on bigger games. Use something
# more robust instead.
# My main goal was to learn how graphic APIs work, and it was
# achieved.
#
# Functionality:
# __ Control         - base class for all UI elements. Has position,
#                      size and can have child controls.
#  \____ ColorRect   - a colored rectangle with an optional outline.
#      \____ Button  - a pressable ColorRect with a child control
#                      attached to it.
#  \____ Label       - a colored text.
#  \____ TextureRect - a rectangle with a texture attached to it,
#                      which can be reused.
#  \____ Scroll      - a container that arranges child controls
#        Container     vertically or horizontally with an
#                      optional scrollbar.
#
# __ ShaderPlane     - a rectangle with a shader program applied
#                      to it. You can automatically get uniform
#                      locations and provide their types.



import sys

USE_MODULES = ["mainloop", "variant", "post_processing"]
post_processing = None
PIXEL_SIZE = None
CHUNK_PIXEL_SIZE = None
plane_offset_x, plane_offset_y = 0,0
variant = None
CHUNK_SIZE = 12
mainloop = None
Input = None
WINDOW_WIDTH = None
WINDOW_HEIGHT = None
MAX_CHUNKS = 10000

modules_dict = {}

from OpenGL.GL import *
import OpenGL.GLUT as glut
import numpy as np
from PIL import Image, ImageFont, ImageDraw

_control_types: dict = {}

def get_vertex_offset():
    return (plane_offset_x - mainloop.CHUNKS_RECT[0] * CHUNK_SIZE * CHUNK_PIXEL_SIZE,
            plane_offset_y - mainloop.CHUNKS_RECT[1] * CHUNK_SIZE * CHUNK_PIXEL_SIZE)

def cull(self):
    if not self.visible: return False
    xmin, ymin, xmax, ymax = 0, 0, mainloop.WINDOW_WIDTH, mainloop.WINDOW_HEIGHT
    scale_x, scale_y = self.scale_x, self.scale_y
    if self.root.__class__ == ScrollContainer:
        xmin, ymin, xmax, ymax = self.root.x - self.root.margin_left, self.root.y - self.root.margin_bottom, self.root.x + self.root.scale_x, self.root.y + self.root.scale_y
    ret = xmin-scale_x < self.x < xmax and ymin-scale_y < self.y < ymax# and self in _culled
    return ret

_controls = []


from collections import deque
class Control:
    PIPELINE_ID = 0
    self_storage = []
    buffer = []
    data_slots = {}

    @classmethod
    def get_data_slot(cls):
        return cls.data_slots.setdefault(cls.PIPELINE_ID, {})
    @classmethod
    def _class_created(cls):
        pass

    def __init_subclass__(cls, /, **kwargs):
        _control_types[cls] = cls.self_storage
        cls.buffer = list()
        cls.self_storage = []
        cls._class_created()

    __slots__ = ("x", "y", "margin_left", "margin_bottom",
                 "scale_x", "scale_y",
                 "color", "child_controls", "local_x",
                 "local_y", "init_scale", "metadata",
                 "parent", "root",
                 "visible", "mouse_in", "_z_index",
                 "data_snapshot",
                 "was_updated")

    def hide(self): self.visible = False
    def show(self): self.visible = True

    def make_data_snapshot(self):
        gen = self._generate_data()
        if gen != self.data_snapshot:
            self.was_updated = True
            self.data_snapshot = gen

    def _generate_data(self) -> tuple:
        return (self.x, self.y, self.scale_x, self.scale_y)

    @property
    def z_index(self):
        return self._z_index

    @z_index.setter
    def z_index(self, val):
        global prev_control_count
        self._z_index = val
        prev_control_count = 0

    @z_index.getter
    def z_index(self):
        return self._z_index

    def __init__(self, *args, **kwargs):
        _controls.append(self)

        self.was_updated = True
        self.verts = None
        self.child_controls = []
        self._z_index = 0
        self.self_storage.append(self)
        self.margin_left = 0
        self.margin_bottom = 0
        self.metadata = {}
        self.root = None
        self.visible = True
        self.init_scale = control_scale
        self.mouse_in = False
        self.parent = None
        if __class__ == Control:
            self.x, self.y, self.scale_x, self.scale_y = 0, 0, 1, 1
        self._ready(*args, **kwargs)
        self.data_snapshot = self._generate_data()
    def set_meta(self, name: str, v):
        self.metadata[name] = v

    def has_meta(self, name: str):
        return name in self.metadata

    def get_meta(self, name: str):
        return self.metadata.get(name)

    def _ready(self, *args, **kwargs):
        pass

    def add_child(self, control: "Control"):
        if self.root is None:
            queue = deque(control.child_controls + [control])
            while queue:
                ctrl = queue.popleft()
                ctrl.root = self
                queue.extend(ctrl.child_controls)

        control.local_x = control.x
        control.parent = self
        control.local_y = control.y
        self.child_controls.append(control)
    def add_children(self, *args: tuple["Control"]):
        for control in args:
            self.add_child(control)

    @classmethod
    def _draw_stage_exited(cls):
        glColor4f(1, 1, 1, 1)

    @classmethod
    def _draw_stage_entered(cls):
        pass

    @classmethod
    def draw_stage_exited(cls):
        cls._draw_stage_exited()

    @classmethod
    def draw_stage_entered(cls):
        cls._draw_stage_entered()

    def __contains__(self, item):
        return item in self.child_controls

    def _before_draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.scale_x, self.scale_y, 1.0)
    def _after_draw(self):
        glPopMatrix()

    def update_mouse_in(self):
        screen_pos = mainloop.screen_mouse_position
        pos = variant.Vector2(screen_pos[0], (mainloop.WINDOW_HEIGHT - screen_pos[1]), i=True)
        self.mouse_in = self.x <= pos.x <= self.x + self.scale_x and self.y <= pos.y <= self.y + self.scale_y

    def draw(self):
        #self.make_data_snapshot()

        for child in self.child_controls:
            child.x = child.local_x + self.x
            child.y = child.local_y + self.y

        if cull(self):
            self._before_draw()
            self._draw()
            self._after_draw()

    def _draw(self):
        pass
    def _free(self):
        pass
    def free(self):
        self._free()
        _controls.remove(self)
        self.self_storage.remove(self)

bitmaps = {}

def _make_text_bitmap(text: str, font_path: str, font_size: int, margin=0):
    font_path = os.path.abspath(font_path) if not os.path.isabs(font_path) else font_path
    args = (text, font_path, font_size, margin)
    if args in bitmaps: return bitmaps[args]

    font = ImageFont.truetype(font_path, font_size)

    tmp_img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    tmp_draw = ImageDraw.Draw(tmp_img)
    left, top, right, bottom = tmp_draw.textbbox((0, 0), text, font=font)

    width  = right - left + margin
    height = bottom - top + margin

    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=(255,255,255,255))

    raw_bytes = image.tobytes("raw", "RGBA", 0, -1)

    bitmaps[args] = (width, height, raw_bytes)

    return width, height, raw_bytes

import os

control_scale: float = 1.0

def set_control_scale(v: float):
    global control_scale
    control_scale = v


class Label(Control):
    self_storage = []

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        value = value.lower()
        self._text = value
        self.width, self.height, self.raw = _make_text_bitmap(self._text,
        "../main/assets/Pixel Emulator.otf", 25,
        margin=10)

    @text.getter
    def text(self) -> str:
        return self._text

    def _ready(self, text, x:int, y:int, scale: tuple = (1.0, 1.0), color: tuple = (1.0, 1.0, 1.0, 1.0)):
        self.color = color; self.scale_x, self.scale_y = scale[0]*control_scale, scale[1]*control_scale
        self._text = ""
        self.text, self.x, self.y = text.lower(), int(x), int(y)
        self.z_index = 1
    def _before_draw(self):
        pass
        #glColor4f(*self.color)
    def _after_draw(self):
        pass
        #glPopMatrix()
    def _draw(self):

        glColor4f(*self.color)
        glPushAttrib(GL_PIXEL_MODE_BIT | 0x00000010)#GL_PIXEL_TRANSFER_BIT)
        glPixelTransferf(GL_RED_SCALE, self.color[0]); glPixelTransferf(GL_GREEN_SCALE, self.color[1])
        glPixelTransferf(GL_BLUE_SCALE, self.color[2]); glPixelTransferf(GL_ALPHA_SCALE, self.color[3])
        glPixelZoom(self.scale_x, self.scale_y)
        glRasterPos2i(int(self.x), int(self.y))
        glDrawPixels(self.width, self.height, GL_RGBA, GL_UNSIGNED_BYTE, self.raw)
        glPopAttrib()
class ColorRect(Control):
    self_storage = []

    def _ready(self, x, y, size: tuple = (1.0, 1.0),
               color: tuple = (1.0, 1.0, 1.0, 1.0),
               outline_width: float = 0,
               outline_color: tuple = (1.0, 1.0, 1.0, 1.0),
               offsets_fix = 1,
                *args):

        self.offsets_fix = offsets_fix
        self.color = [*color]; self.scale_x, self.scale_y = int(size[0]*control_scale), int(size[1]*control_scale)
        self.x, self.y = int(x*control_scale), int(y*control_scale); self.outline_color = outline_color
        self.outline_width = int(outline_width*control_scale)

    @classmethod
    def _draw_stage_entered(cls):
        glBegin(GL_TRIANGLES)

    @classmethod
    def _class_created(cls):
        cls.datas = {}
        cls.buffer = []
        cls._outline_data = None



    @classmethod
    def _draw_stage_exited(cls):
        #print("END")
    #    print(__class__.is_draw_stage())
        #  super()._draw_stage_exited
        glEnd()



        for self in __class__.buffer:
            if self.outline_width == 0: continue

            width = self.outline_width
            glLineWidth(width)
            width *= self.offsets_fix
            glColor4f(*self.outline_color)

            glBegin(GL_LINES)
            glVertex2f(self.x, self.y + width / 2)
            glVertex2f(self.x + self.scale_x, self.y + width / 2)

            glVertex2f(self.x + self.scale_x - width / 2, self.y)
            glVertex2f(self.x + self.scale_x - width / 2, self.y + self.scale_y)

            glVertex2f(self.x + self.scale_x, self.y + self.scale_y - width / 2)
            glVertex2f(self.x, self.y + self.scale_y - width / 2)

            glVertex2f(self.x + width / 2, self.y + self.scale_y)
            glVertex2f(self.x + width / 2, self.y)
            glEnd()

        glLineWidth(1.0)

    def _generate_data(self) -> tuple:
        return (self.x, self.y, self.scale_x, self.scale_y, self.outline_color, self.color)

    def _after_draw(self):
        pass

    def _before_draw(self):
        pass

    def _draw(self):
        if self.color[3] > 0:
            glColor4f(*self.color)


            glVertex2f(self.x, self.y)
            glVertex2f(self.x+self.scale_x, self.y)
            glVertex2f(self.x+self.scale_x, self.y+self.scale_y)

            glVertex2f(self.x, self.y)
            glVertex2f(self.x + self.scale_x, self.y + self.scale_y)
            glVertex2f(self.x, self.y+self.scale_y)
        #glRectf(0.0f, 0.0f, w, h)




from enum import Enum
class PressState(Enum):
    RELEASED = 0
    JUST_PRESSED = 1
    PRESSED = 2
    JUST_RELEASED = 3


def default_call(from_button: "Button"):
    pass
    #print(from_button)
datas = {}
from math import floor
class ScrollContainer(Control):
    self_storage = []
    def _ready(self, x: int, y: int, size: tuple[int, int], padding: int = 10, direction: str = "v", scroll_bar: ColorRect = None):
        self.x, self.y, self.scale_x, self.scale_y = int(x * control_scale), int(y * control_scale), size[0] * control_scale, size[1] * control_scale
        self.child_controls = []; self.value = 0.0
        self.padding = padding * control_scale; self.direction = direction
        self.smooth_scroll = False; self.child_pixels = 0
        self.scroll_k = -500.0; self._value_target = 0.0
        self.scroll_lerp_speed = 20.0
        self.scroll_enabled = True; self.value_mapped = 0
        self.snap = 0
        self.out_of_bounds_scroll_on = False
        self._prev = 0
        self.scroll_bar = scroll_bar#ColorRect(90,20,(50,10),outline_width=0)

    @classmethod
    def _draw_stage_entered(cls):
        pass

    @classmethod
    def _draw_stage_exited(cls):
        pass

    def _before_draw(self):
        pass

    def _after_draw(self):
        pass

    def scroll(self, delta_px: float):
        scroll_range = max(self.child_pixels, 0)

        raw_off = self._prev * scroll_range + delta_px / self.child_pixels * 100.0

        #snapped = raw_off

        snapped = variant.clamp(raw_off, 0, scroll_range)

        self._value_target = (snapped / scroll_range) if scroll_range > 0 else 0.0
        self._prev = self._value_target



    def _scroll_process(self):
        screen_pos = mainloop.screen_mouse_position
        pos = variant.Vector2(screen_pos[0], (mainloop.WINDOW_HEIGHT - screen_pos[1]), i=True)
        if (self.x <= pos.x <= self.x+self.scale_x and self.y <= pos.y <= self.y+self.scale_y) or self.out_of_bounds_scroll_on:
            self.scroll(self.scroll_k * mainloop.mouse_scroll_y * 400 / 1000)

        if self.scroll_bar is not None:
            if self.direction == "h":
                self.scroll_bar.x = variant.lerp(self.x, self.x + self.scale_x - self.scroll_bar.scale_x, self.value)
                self.scroll_bar.scale_x = (self.scale_x**2 / self.child_pixels)
            else:
                self.scroll_bar.y = variant.lerp(self.x, self.y + self.scale_y - self.scroll_bar.scale_y, self.value)
                self.scroll_bar.scale_y = (self.scale_y**2 / self.child_pixels)
            #print(self.scale_x / self.child_pixels)
        #self.scroll_bar.x = self.scale_x * self.value
        #print()
        if self.smooth_scroll:
            self.value = variant.lerp(self.value, self._value_target, mainloop.delta_time * self.scroll_lerp_speed)
        else:
            self.value = self._value_target
        self.value_mapped = self.value * -(self.child_pixels - self.scale_x + 20)# * self.init_scale

    def _draw(self):
      #  print(self.child_pixels, self.scale_x)
        if self.scroll_enabled and self.child_pixels > self.scale_x:
            self._scroll_process()
        h = self.direction == "h"
        caret = 0
        for control in self.child_controls:
            if h:
                control.local_x = caret + self.value_mapped
                caret += control.scale_x
            else:
                control.local_y = caret + self.value_mapped
                caret += control.scale_y
            self.child_pixels = caret
            caret += self.padding

bufid = 0

class Button(ColorRect):

    def _generate_data(self) -> tuple:
        return (self.x, self.y, self.scale_x, self.scale_y, id(self.outline_color), id(self.color), self.press_state)

    @classmethod
    def _class_created(cls):
        cls.buffer = []

    def _ready(self, x, y, size: tuple = (1.0, 1.0),
                color: tuple = (1.0, 1.0, 1.0, 1.0),
                outline_width: float = 0,
                outline_color: tuple = (1.0, 1.0, 1.0, 1.0),
                label = None,
                press_state_update: callable = default_call,
                color_hovered: tuple = (1.0,1.0,1.0,1.0),
                color_pressed: tuple = (1.0,1.0,1.0,1.0),
               offsets_fix = 1):
        super()._ready(x, y,size,color,outline_width,outline_color,offsets_fix=offsets_fix)
        self.label = label
        if not label is None:
            self.add_child(label)
            label.local_x = int(label.x*control_scale); label.y = int(label.y*control_scale)
        #label.local_y += int(x*control_scale); label.y += int(y*control_scale)
        self.press_state_update = press_state_update; self.press_state = PressState.RELEASED
        self.color_hovered, self.color_pressed = color_hovered, color_pressed
        self.color_default = color
        self.stay_pressed = False
        self.double = False
        self.held = False

    def reset(self):
        self.press_state = PressState.RELEASED

    def press(self):
        self.color = self.color_pressed
        self.press_state = PressState.JUST_PRESSED
        self.press_state_update(self)

    def _draw(self):
        if mainloop.mouse_just_pressed and self.mouse_in and self.held and self.double and self.press_state == PressState.JUST_PRESSED:
            self.press_state = PressState.JUST_RELEASED
            self.held = False
            super()._draw(); return

        if self.mouse_in or ((self.stay_pressed or self.double) and self.press_state == PressState.JUST_PRESSED):

            self.color = self.color_hovered if self.press_state != PressState.PRESSED else self.color_pressed

            if (self.stay_pressed or self.double) and self.press_state == PressState.JUST_PRESSED:
                #print("JFHJFJ")
                self.held = True
                self.color = self.color_pressed
                super()._draw(); return
        else:
            self.color = self.color_default


        if mainloop.mouse_just_pressed and self.mouse_in and (self.press_state == PressState.RELEASED or self.press_state == PressState.JUST_RELEASED):
            self.press_state = PressState.JUST_PRESSED
        elif mainloop.mouse_pressed and self.mouse_in:
            self.press_state = PressState.PRESSED
        elif not mainloop.mouse_pressed and (self.press_state == PressState.PRESSED or self.press_state == PressState.JUST_PRESSED):
            self.press_state = PressState.JUST_RELEASED
        else:
            self.press_state = PressState.RELEASED
        self.press_state_update(self)


        super()._draw()


_TILE_OFFSETS = None

def _init_tile_offsets():
    global _TILE_OFFSETS
    coords = np.zeros((CHUNK_SIZE * CHUNK_SIZE, 2), dtype=np.float32)
    idx = 0
    for y in range(CHUNK_SIZE):
        for x in range(CHUNK_SIZE):
            coords[idx, 0] = x * CHUNK_PIXEL_SIZE
            coords[idx, 1] = y * CHUNK_PIXEL_SIZE
            idx += 1
    _TILE_OFFSETS = coords

textures = {}
textures: dict[str, tuple[int, int, int]] = {}

_quad_vbo_positions = None
_quad_vbo_texcoords = None

def _init_quad_vbo():
    global _quad_vbo_positions, _quad_vbo_texcoords
    positions = np.array([0, 0,
                           1, 0,
                           0, 1,
                           1, 1], dtype=np.float32)
    texcoords = np.array([0, 0,
                          1, 0,
                          0, 1,
                          1, 1], dtype=np.float32)
    _quad_vbo_positions = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, _quad_vbo_positions)
    glBufferData(GL_ARRAY_BUFFER, positions.nbytes, positions, GL_STATIC_DRAW)

    _quad_vbo_texcoords = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, _quad_vbo_texcoords)
    glBufferData(GL_ARRAY_BUFFER, texcoords.nbytes, texcoords, GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, 0)


def load_texture(path: str, linear: bool = False):
    img_path = os.path.abspath(path) if not os.path.isabs(path) else path

    img = Image.open(img_path).transpose(Image.FLIP_TOP_BOTTOM)
    img = img.convert("RGBA")
    width, height = img.size
    data = img.tobytes()

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    wrap = GL_CLAMP_TO_EDGE
    filter_min = GL_LINEAR_MIPMAP_LINEAR if linear else GL_NEAREST
    filter_mag = GL_LINEAR if linear else GL_NEAREST
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, wrap)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, wrap)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, filter_min)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, filter_mag)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

    glBindTexture(GL_TEXTURE_2D, 0)
    return tex_id, width, height


def add_texture(path: str, name: str, linear: bool = False):
    textures[name] = load_texture(path, linear)

class TextureRect(Control):
    def set_texture(self, name: str):
        self.texture_id, self.width, self.height = textures[name]

    def _ready(self, path: str, name: str, linear: bool = False):
        if name in textures:
            self.texture_id, self.width, self.height = textures[name]
        else:
            textures[name] = load_texture(path, linear)
            self.texture_id, self.width, self.height = textures[name]

    @classmethod
    def _draw_stage_entered(cls):
        pass

    def _before_draw(self):
        pass

    def _after_draw(self):
        pass

    @classmethod
    def _draw_stage_exited(cls):
        pass

    def _draw(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.width * self.scale_x, self.height * self.scale_y, 1)

        glEnableClientState(GL_VERTEX_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, _quad_vbo_positions)
        glVertexPointer(2, GL_FLOAT, 0, None)

        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, _quad_vbo_texcoords)
        glTexCoordPointer(2, GL_FLOAT, 0, None)

        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)


class RenderChunk:
    __slots__ = ('grid_x', 'grid_y', 'start_index')
    def __init__(self, gx: int, gy: int, start_idx: int):
        self.grid_x = gx
        self.grid_y = gy
        self.start_index = start_idx
    def update(self, data):
        start = self.start_index
        _id_buffer[start:start + len(data)] = data

_render_chunks = []
_total_count = 0
_pos_vbo = None
_id_vbo = None
_id_buffer = None

_program = None

def compile_shader(src: str, kind: int):
    sh = glCreateShader(kind)
    glShaderSource(sh, src)
    glCompileShader(sh)
    if glGetShaderiv(sh, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(sh).decode())
    return sh


uniforms_locations = {}
def link_program(vs, fs, get_uniforms=None, uniform_namespace=uniforms_locations):
    prog = glCreateProgram()
    glAttachShader(prog, vs)
    glAttachShader(prog, fs)
    glLinkProgram(prog)
    if glGetProgramiv(prog, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(prog).decode())
    if not get_uniforms is None:
        for uniform in get_uniforms:
            uniform_namespace[uniform] = glGetUniformLocation(prog, uniform.encode("utf-8"))
    return prog

render_chunk_origins = {}
mv = None
from array import array
def add_chunk(gx, gy, data: array) -> RenderChunk:
    global _total_count, _render_chunks, _id_buffer, mv

    if (gx,gy) in render_chunk_origins:
        return render_chunk_origins[(gx,gy)]

    start_idx = _total_count
    new_chunk = RenderChunk(gx, gy, start_idx)
    render_chunk_origins[(gx,gy)] = new_chunk

    _render_chunks.append(new_chunk)
    _total_count += CHUNK_SIZE * CHUNK_SIZE

    if _id_buffer is None:
        _id_buffer = array("L", [0]*(CHUNK_SIZE*CHUNK_SIZE))#np.zeros(_total_count, dtype=np.int32)
    else:
        mv = None
        new_buf = array("L", [0]*_total_count)
        new_buf[:len(_id_buffer)] = _id_buffer
        _id_buffer = new_buf
        #new_buf = np.zeros(_total_count, dtype=np.int32)
        #new_buf[:_id_buffer.shape[0]] = _id_buffer
        #_id_buffer = new_buf

    mv = memoryview(_id_buffer)

    base = np.array([gx * CHUNK_SIZE * CHUNK_PIXEL_SIZE + (plane_offset_x - mainloop.CHUNKS_RECT[0] * CHUNK_SIZE * CHUNK_PIXEL_SIZE),
                     gy * CHUNK_SIZE * CHUNK_PIXEL_SIZE + (plane_offset_y - mainloop.CHUNKS_RECT[1] * CHUNK_SIZE * CHUNK_PIXEL_SIZE)], dtype=np.float32)
    pos_chunk = (_TILE_OFFSETS + base).flatten()
    byte_off_pos = new_chunk.start_index * 2 * 4
    glBindBuffer(GL_ARRAY_BUFFER, _pos_vbo)
    glBufferSubData(GL_ARRAY_BUFFER, byte_off_pos, pos_chunk)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    #flat_ids = data#.flatten().astype(np.int32)
    mv[start_idx:start_idx + len(data)] = data

    return new_chunk

prev_control_count = 0
sorted_controls = []

plane = None
def _ready():
    global plane

    re.flush()

    _init_quad_vbo()
    glClampColor(GL_CLAMP_VERTEX_COLOR, GL_FALSE)
    glClampColor(GL_CLAMP_FRAGMENT_COLOR, GL_FALSE)
    # for control_type in [Control, Label, ColorRect, Button, ScrollContainer]:
    #     _control_types[control_type] = control_type.self_storage
    glClearColor(0.3, 0.3, 0.3, 0)

    global _program, _pos_vbo, _id_vbo, _id_buffer
    glut.glutInit()

    plane = ShaderPlane("shaders/vertex.glsl", "shaders/fragment.glsl", generate_vao = False, get_uniforms=["uPalette"])
    plane.set_shader_parameter_type("uPalette", "glUniform4fv")
    plane.set_shader_parameter("uPointSize", CHUNK_PIXEL_SIZE)
    glUseProgram(plane.program_id)
    plane.set_uniforms()
    glUseProgram(0)
    _program = plane.program_id

    _init_tile_offsets()

    _pos_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, _pos_vbo)
    glBufferData(GL_ARRAY_BUFFER,
                 MAX_CHUNKS * CHUNK_SIZE * CHUNK_SIZE * 2 * 4,
                 None,
                 GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    _id_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, _id_vbo)
    glBufferData(GL_ARRAY_BUFFER,
                 MAX_CHUNKS * CHUNK_SIZE * CHUNK_SIZE * array("L", [0]).itemsize,
                 None,
                 GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_PROGRAM_POINT_SIZE)


_gradients = []
def create_gradient(x,y,w,h, topright = (0,0,0,0), botright = (0,0,0,0), topleft = (0,0,0,1), botleft = (0,0,0,1)):
    _gradients.append((x,y,w,h,topright,botright,topleft,botleft))


def draw_colored_quad(x,y,w,h, topright = (0,0,0,0), botright = (0,0,0,0), topleft = (0,0,0,1), botleft = (0,0,0,1)):
    glColor4f(*botleft)
    glVertex2f(x,y)
    glColor4f(*botright)
    glVertex2f(x+w,y)
    glColor4f(*topright)
    glVertex2f(x+w,y+h)
    glColor4f(*topleft)
    glVertex2f(x,y+h)

compiled_shaders = {}
compiled_programs = {}

import modules.reimport as re
@re.reimport("render", variant=variant)
class ShaderPlane:
    __slots__ = ("program_id", "uniforms", "vs_path", "fs_path", "uniform_changes_enqueued", "uniform_type_map", "vao", "vbo")
    def set_shader_parameter(self, name: str, *values):
        self.uniform_changes_enqueued[name] = values
    def set_shader_parameter_type(self, name: str, type_call_name: str):
        self.uniform_type_map[name] = getattr(sys.modules["render"], type_call_name)

    def set_uniforms(self):
        #1, GL_TRUE, proj.flatten()
        for name, values in self.uniform_changes_enqueued.items():
            self.uniform_type_map.get(name, glUniform1f)(self.uniforms[name], *values)
        self.uniform_changes_enqueued.clear()

    def generate_buffers(self, x,y,w,h):

        quad = np.array([
            # x, y,   r, g, b, a
            x,   y,   1, 1, 1, 1,
            x+w, y,   1, 1, 1, 1,
            x+w, y+h, 1, 1, 1, 1,
            x,   y+h, 1, 1, 1, 1,
        ], dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)

        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, quad.nbytes, quad, GL_DYNAMIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, False, 6 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 4, GL_FLOAT, False, 6 * 4, ctypes.c_void_p(2 * 4))

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def __init__(self, vs_path, fs_path, get_uniforms = None, program_reuse_name: str = "", x=0, y=0, w=200, h=200, generate_vao = True, set_default_uniforms = True):

        get_uniforms = ["uPointSize", "uProj"] if get_uniforms is None else get_uniforms + ["uPointSize", "uProj"]
        self.uniforms, self.uniform_changes_enqueued = {}, {}
        self.uniform_type_map = {"uProj": glUniformMatrix4fv, "uPointSize": glUniform1f}
        if generate_vao:
            self.generate_buffers(x, y, w, h)

        shader_map = compiled_shaders
        if not vs_path in shader_map:
            shader_map[vs_path] = compile_shader(variant.read_asset(vs_path), GL_VERTEX_SHADER)
        vs = shader_map[vs_path]

        if not fs_path in shader_map:
            shader_map[fs_path] = shader_map.setdefault(fs_path, compile_shader(variant.read_asset(fs_path), GL_FRAGMENT_SHADER))
        fs = shader_map[fs_path]

        program_map = compiled_programs if program_reuse_name else {}

        if not program_reuse_name in program_map:
            program_map[program_reuse_name] = link_program(vs, fs, get_uniforms, self.uniforms), self.uniforms, self.uniform_type_map
        self.program_id, self.uniforms, self.uniform_type_map = program_map[program_reuse_name]

        proj = np.array([
            [2.0 / WINDOW_WIDTH, 0, 0, -1],
            [0, 2.0 / WINDOW_HEIGHT, 0, -1],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)

        if set_default_uniforms:
            self.set_shader_parameter("uProj", 1, GL_TRUE, proj.flatten())
            self.set_shader_parameter("uPointSize", CHUNK_PIXEL_SIZE)
            glUseProgram(self.program_id)
            self.set_uniforms()
            glUseProgram(0)

    def flush(self):
        glUseProgram(self.program_id)
        self.set_uniforms()
        glUseProgram(0)

    def _process(self):
        self.set_uniforms()
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)


shader_planes: list[ShaderPlane] = []


def add_shader_plane(plane: ShaderPlane):
    shader_planes.append(plane)


prev_plane_count = 0
sorted_planes = []
def _shader_plane_pass():
    if not shader_planes: return
    global prev_plane_count, sorted_planes

    if prev_plane_count != len(shader_planes):
        prev_plane_count = len(shader_planes)
        sorted_planes = sorted(shader_planes, key=lambda plane: plane.program_id)


    for plane in sorted_planes:
        glUseProgram(plane.program_id)


        #draw_colored_quad(0,0,900,900,(1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,1))

        plane._process()
    glUseProgram(0)
    glBindVertexArray(0)


def _draw_chunk_pass():
    global _id_buffer
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(_program)

    glBindBuffer(GL_ARRAY_BUFFER, _id_vbo)
    glBufferSubData(GL_ARRAY_BUFFER, 0, bytes(mv))

    glBindBuffer(GL_ARRAY_BUFFER, _pos_vbo)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)

    glBindBuffer(GL_ARRAY_BUFFER, _id_vbo)
    glEnableVertexAttribArray(1)
    glVertexAttribIPointer(1, 1, GL_INT, 0, None)

    glDrawArrays(GL_POINTS, 0, _total_count)

    glDisableVertexAttribArray(1)
    glDisableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glUseProgram(0)



def _draw_control_pass():
    # set up orthographic projection for UI
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor4f(1.0, 1.0, 1.0, 1.0)

    for t in _control_types:
        t.PIPELINE_ID = 0

    if _controls:
        global sorted_controls, prev_control_count
        if len(_controls) != prev_control_count:
            sorted_controls = sorted(
                _controls,
                key=lambda c: (c.z_index, id(c.__class__))
            )
        prev_control_count = len(_controls)

        prev_pipeline = None
        for control in sorted_controls:
            control.update_mouse_in()
            culled = cull(control)

            if not isinstance(control, ScrollContainer) \
               and not culled \
               and not control.child_controls:
                control.mouse_in = False
                continue

            pipeline_cls = ColorRect if isinstance(control, ColorRect) else control.__class__

            if prev_pipeline is None or prev_pipeline is not pipeline_cls:
                if prev_pipeline is not None:
                    prev_pipeline.draw_stage_exited()
                    prev_pipeline.buffer.clear()
                pipeline_cls.PIPELINE_ID += 1
                pipeline_cls.draw_stage_entered()
            prev_pipeline = pipeline_cls

            control.draw()
            if culled:
                pipeline_cls.buffer.append(control)

        if prev_pipeline is not None:
            prev_pipeline.draw_stage_exited()
            prev_pipeline.buffer.clear()
  #  for c in sorted_controls:
#        c.was_updated = False

def _draw_gradient_pass():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glBegin(GL_QUADS)
    for gradient in _gradients:
        draw_colored_quad(*gradient)#[0],gradient[1],gradient[2],gradient[3],gradient[4],gradient[5],gradient[6],gradient[7])
    glEnd()

    glPopMatrix()


def _draw_matrix_clear():
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)



def _process(delta: float):
    glDisable(GL_BLEND)
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glClear(GL_COLOR_BUFFER_BIT)
    post_processing.open_framebuffer()


    _draw_chunk_pass()
    post_processing.close_framebuffer()
    post_processing.draw_framebuffer()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    _shader_plane_pass()
    _draw_control_pass()
    _draw_gradient_pass()
    _draw_matrix_clear()

