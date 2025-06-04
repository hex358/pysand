import mainloop

USE_MODULES = ["mainloop", "variant"]
PIXEL_SIZE = None
variant = None
CHUNK_SIZE = 16
WINDOW_WIDTH = None
WINDOW_HEIGHT = None
MAX_CHUNKS = 10000

modules_dict = {}

from OpenGL.GL import *
import OpenGL.GLUT as glut
import numpy as np

_control_types: dict = {}



class Control:
    self_storage = []
    __slots__ = ("x", "y", "scale_x", "scale_y", "color")
    def __init__(self, *args, **kwargs):
        self.self_storage.append(self)
        self._ready(*args, **kwargs)

    def _ready(self, *args, **kwargs):
        pass

    @staticmethod
    def _draw_stage_entered():
        pass

    @staticmethod
    def _draw_stage_exited():
        glColor4f(1, 1, 1, 1)

    def _before_draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.scale_x, self.scale_y, 1.0)
    def _after_draw(self):
        glPopMatrix()
    def draw(self):
        self._before_draw()
        self._draw()
        self._after_draw()
    def _draw(self):
        pass
    def _free(self):
        pass
    def free(self):
        self._free()
        self.self_storage.remove(self)


from PIL import Image, ImageFont, ImageDraw
def _make_text_bitmap(text: str, font_path: str, font_size: int, color=(1.0,1.0,1.0,1.0), margin=0):
    font = ImageFont.truetype(font_path, font_size)

    tmp_img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    tmp_draw = ImageDraw.Draw(tmp_img)
    left, top, right, bottom = tmp_draw.textbbox((0, 0), text, font=font)

    width  = right - left + margin
    height = bottom - top + margin

    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=tuple(int(i*255) for i in color))

    raw_bytes = image.tobytes("raw", "RGBA", 0, -1)

    return width, height, raw_bytes

import os
class Label(Control):
    self_storage = []
    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self.width, self.height, self.raw = _make_text_bitmap(self._text,
        os.path.abspath("../main/shaders/Pixel Emulator.otf"), 25, self.color,
        margin=10)

    @text.getter
    def text(self) -> str:
        return self._text

    def _ready(self, text, x, y, scale: tuple = (1.0, 1.0), color: tuple = (1.0, 1.0, 1.0, 1.0)):
        self.color = color; self.scale_x, self.scale_y = scale[0], scale[1]
        self._text = ""
        self.text, self.x, self.y = text, x, y
    def _before_draw(self):
        pass
    def _after_draw(self):
        pass
        #glPopMatrix()
    def _draw(self):
        glPushAttrib(GL_PIXEL_MODE_BIT)
        glPixelZoom(self.scale_x, self.scale_y)
        glRasterPos2i(self.x, self.y)
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
        self.color = color; self.scale_x, self.scale_y = size[0], size[1]
        self.x, self.y = x, y; self.outline_color = outline_color
        self.outline_width = outline_width

    @staticmethod
    def _draw_stage_entered():
        glBegin(GL_TRIANGLES)

    @staticmethod
    def _draw_stage_exited():
        #print("END")
        glEnd()

        for self in __class__.self_storage:
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

class Button(ColorRect):

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
        assert(label is not None, "Label can't be None")
        self.label = label
        label.x += x; label.y += y
        self.press_state_update = press_state_update
        self.color_hovered, self.color_pressed = color_hovered, color_pressed
        self.color_default = color
        self.mouse_in = False
        self.press_state = PressState.RELEASED

    def _draw(self):
        screen_pos = mainloop.screen_mouse_position
        pos = variant.Vector2(screen_pos[0], (WINDOW_HEIGHT - screen_pos[1]), i=True)
        self.mouse_in = self.x <= pos.x <= self.x+self.scale_x and self.y <= pos.y <= self.y+self.scale_y

        if self.mouse_in:
            self.color = self.color_hovered if self.press_state != PressState.PRESSED else self.color_pressed
        else:
            self.color = self.color_default


        if mainloop.mouse_just_pressed and self.mouse_in and (self.press_state == PressState.PRESSED or self.press_state == PressState.JUST_PRESSED):

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
            coords[idx, 0] = x * PIXEL_SIZE
            coords[idx, 1] = y * PIXEL_SIZE
            idx += 1
    _TILE_OFFSETS = coords

class RenderChunk:
    __slots__ = ('grid_x', 'grid_y', 'start_index')
    def __init__(self, gx: int, gy: int, start_idx: int):
        self.grid_x = gx
        self.grid_y = gy
        self.start_index = start_idx
    def update(self, data: np.ndarray):
        global _id_buffer
        flat_ids = data.flatten().astype(np.int32)
        start = self.start_index
        _id_buffer[start:start + flat_ids.size] = flat_ids

_render_chunks = []
_total_count = 0
_pos_vbo = None
_id_vbo = None
_id_buffer = None

_program = None
_uProj = None
_uPointSize = None

def compile_shader(src: str, kind: int):
    sh = glCreateShader(kind)
    glShaderSource(sh, src)
    glCompileShader(sh)
    if glGetShaderiv(sh, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(sh).decode())
    return sh


def link_program(vs, fs):
    prog = glCreateProgram()
    glAttachShader(prog, vs)
    glAttachShader(prog, fs)
    glLinkProgram(prog)
    if glGetProgramiv(prog, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(prog).decode())
    return prog

def add_chunk(gx, gy, data: np.ndarray) -> RenderChunk:
    global _total_count, _render_chunks, _id_buffer
    start_idx = _total_count
    new_chunk = RenderChunk(gx, gy, start_idx)
    _render_chunks.append(new_chunk)
    _total_count += CHUNK_SIZE * CHUNK_SIZE

    if _id_buffer is None:
        _id_buffer = np.zeros(_total_count, dtype=np.int32)
    else:
        new_buf = np.zeros(_total_count, dtype=np.int32)
        new_buf[:_id_buffer.shape[0]] = _id_buffer
        _id_buffer = new_buf

    base = np.array([gx * CHUNK_SIZE * PIXEL_SIZE,
                     gy * CHUNK_SIZE * PIXEL_SIZE], dtype=np.float32)
    pos_chunk = (_TILE_OFFSETS + base).flatten()
    byte_off_pos = new_chunk.start_index * 2 * 4
    glBindBuffer(GL_ARRAY_BUFFER, _pos_vbo)
    glBufferSubData(GL_ARRAY_BUFFER, byte_off_pos, pos_chunk)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    flat_ids = data.flatten().astype(np.int32)
    _id_buffer[start_idx:start_idx + flat_ids.size] = flat_ids

    return new_chunk


def _ready():
    for control_type in [Control, Label, ColorRect, Button]:
        _control_types[control_type] = control_type.self_storage

    global _program, _uProj, _uPointSize, _pos_vbo, _id_vbo, _id_buffer
    glut.glutInit()

    vs = compile_shader(variant.read_asset("shaders/vertex.glsl"), GL_VERTEX_SHADER)
    fs = compile_shader(variant.read_asset("shaders/fragment.glsl"), GL_FRAGMENT_SHADER)
    _program = link_program(vs, fs)
    glDeleteShader(vs)
    glDeleteShader(fs)

    _uProj = glGetUniformLocation(_program, b"uProj")
    _uPointSize = glGetUniformLocation(_program, b"uPointSize")
    proj = np.array([
        [2.0/WINDOW_WIDTH, 0,               0, -1],
        [0,                2.0/WINDOW_HEIGHT,0, -1],
        [0,                0,              -1,  0],
        [0,                0,               0,  1]
    ], dtype=np.float32)
    glUseProgram(_program)
    glUniformMatrix4fv(_uProj, 1, GL_TRUE, proj.flatten())
    glUniform1f(_uPointSize, PIXEL_SIZE)
    glUseProgram(0)

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
                 MAX_CHUNKS * CHUNK_SIZE * CHUNK_SIZE * 4,
                 None,
                 GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_PROGRAM_POINT_SIZE)

def _process(delta: float):
    global _id_buffer
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(_program)

    glBindBuffer(GL_ARRAY_BUFFER, _id_vbo)
    glBufferSubData(GL_ARRAY_BUFFER, 0, _id_buffer.flatten())

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

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor4f(1.0, 1.0, 1.0, 1.0)

    for control_type in [ColorRect,Button,Label]:
        if len(control_type.self_storage) == 0: continue
        c: type = control_type; c._draw_stage_entered()
        for control in _control_types[control_type]:
            control.draw()
        c._draw_stage_exited()



    glPopMatrix()

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)

    # for control_type in [Label]:
    #     if len(control_type.self_storage) == 0: continue
    #     c: type = control_type; c._draw_stage_entered()
    #     for control in _control_types[control_type]:
    #         control.draw()
    #     c._draw_stage_exited()