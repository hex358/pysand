import os.path

config = []# --create-arrows, ...

UI_MATCH = {
    1: ["SAND", (0.75, 0.69, 0.50, 1.0)],
    2: ["WATER", (0.1,  0.6,  1.0, 1.0)],
    3: ["STONE", (0.7,  0.7,  0.7, 1.0)],
    4: ["WOOD", (0.33,  0.24,  0.19, 1.0)],
    5: ["LAVA", (0.9,  0.4,  0.2, 0.9)],
    6: ["STEAM", (0.7,  0.7,  0.8, 0.7)],
    7: ["DIRT", (0.33,  0.19,  0.19, 1.0)],

}
from random import randint


TAGS = []
USE_MODULES = ["render", "mainloop", "chunk_manager", "*variant", "variant"]
chunk_manager = None
render = None
mainloop = None
CHUNKS_RECT = None
PIXEL_SIZE = None
variant = None
CHUNK_SIZE = None

label = None
modules_dict = {}

hover = None
buttons = {}

rect2 = None
texture = None
plane = None
rect3 = None
scroll2 = None
import numpy as np
def _ready() -> None:
    global label
    global prev_pos
    prev_pos = Vector2(0, 0, i=True)
    label = render.Label("hello",120*5,17*5,(1,1), (1,0,0,1))
    label.z_index = 5
    ox, oy = CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[0], CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[1]

    global rect2
    rect2 = render.ColorRect(
        ox - PIXEL_SIZE*1.333,oy - PIXEL_SIZE*1.333,
        (CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[2] - ox + PIXEL_SIZE*2, CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[3] - oy + PIXEL_SIZE*2),
        (0,0,0,0),PIXEL_SIZE,(0.7,0.7,0.7,1),offsets_fix=1
    )


    render.set_control_scale(0.7)
    buttons["clear"] = render.Button(
        0,0,#110,117,
        (99,35),
        (0.5,0.5,0.5,1),PIXEL_SIZE,(0.8,0.8,0.8,1),
        render.Label("CLEAR",5,5,(1,1), (1,1,1,1)),
        clear_button,
        (0.6, 0.6, 0.6, 1),
        (0.8, 0.8, 0.8, 1),
        offsets_fix=-1,
    )

    buttons["save"] = render.Button(
        0,0,#230,117,
        (92,35),
        (0.5,0.5,0.5,1),PIXEL_SIZE,(0.8,0.8,0.8,1),
        render.Label("SAVE",9,5,(1,1), (1,1,1,1)),
        save_button,
        (0.6, 0.6, 0.6, 1),
        (0.8, 0.8, 0.8, 1),
        offsets_fix=-1,
    )

    buttons["load"] = render.Button(
        0,0,#342,117,
        (88,35),
        (0.5,0.5,0.5,1),PIXEL_SIZE,(0.8,0.8,0.8,1),
        render.Label("LOAD",9,5,(1,1), (1,1,1,1)),
        load_button,
        (0.6, 0.6, 0.6, 1),
        (0.8, 0.8, 0.8, 1),
        offsets_fix=-1,
    )

    buttons["eraser"] = render.Button(
        0,0,#342,117,
        (124,35),
        (0.5,0.5,0.5,1),PIXEL_SIZE,(0.8,0.8,0.8,1),
        render.Label("ERASER",9,5,(1,1), (1,1,1,1)),
        eraser_button,
        (0.6, 0.6, 0.6, 1),
        (0.8, 0.8, 0.8, 1),
        offsets_fix=-1,
    )
    buttons["eraser"].stay_pressed = True


    scroll = render.ScrollContainer(85,117,(800,100),17,"h")
    #scroll.add_children(buttons["load"],buttons["save"],buttons["clear"])
    scroll.add_children(*buttons.values())

    global scroll2
    scroll2 = render.ScrollContainer(80, 39, (480, 70), 17, "h") #975
    scroll2.margin_bottom = 20
    scroll2.scroll_bar = render.ColorRect(180,15,(50,6),outline_width=0,color=(1,1,1,1))
    scroll2.margin_left = 60
    render.create_gradient(80-40,39-21,20,60,botright=(0.3,0.3,0.3,0),topright=(0.3,0.3,0.3,0),
                           topleft=(0.3,0.3,0.3,1),botleft=(0.3,0.3,0.3,1))
    render.create_gradient(394 - (39-17), 39 - 21, 20, 60, botleft=(0.3, 0.3, 0.3, 0), topleft=(0.3, 0.3, 0.3, 0),
                           topright=(0.3, 0.3, 0.3, 1), botright=(0.3, 0.3, 0.3, 1))
    for key in UI_MATCH:
        #if not key in UI_MATCH: key = 3
        color = UI_MATCH[key][1]
        new_button = render.Button(
            0,0,#342,117,
            (65,65),
            color,PIXEL_SIZE,(color[0]/1.6, color[1]/1.6, color[2]/1.6, color[3]),
            render.Label(UI_MATCH[key][0],2,-9,(0.6,0.6), (1,1,1,1)),
            select,
            (color[0]*1.15, color[1]*1.15, color[2]*1.15, 1.0),
            (color[0]*1.15, color[1]*1.15, color[2]*1.15, 1.0),
            offsets_fix=1,
        )
        new_button.stay_pressed = True
        new_button.set_meta("type", key)
        scroll2.add_child(new_button)
    scroll2.snap = 65*0.7+17
    scroll2.smooth_scroll = True
    scroll2.scroll_k = -500.0
    scroll2.smooth_scroll_speed = 390.0

    global rect3
    rect3 = render.ColorRect(80 + 480, 39-50, (800, 120), (0.3, 0.3, 0.3, 1))
    rect3.z_index = 2
    rect4 = render.ColorRect(80 - 200, 39-50, (180, 120), (0.3, 0.3, 0.3, 1))
    rect4.z_index = 2

   # texture = render.TextureRect("../main/ib.png", "ib")

    # texture.x, texture.y = (230,0)
    # texture.z_index = 9
    # texture.scale_x = 1.5
    # texture.scale_y = 1.5

    global plane
    #ox - 1.4*PIXEL_SIZE,oy - 1.1*PIXEL_SIZE,
    plane = render.ShaderPlane("shaders/hovers_vertex.glsl", "shaders/hovers_fragment.glsl",
                               get_uniforms=["mousePos", "shapeSize", "mode", "noiseBits"],
                               x = rect2.x,
                               y = rect2.y,
                               w = rect2.scale_x,
                               h = rect2.scale_y)
    render.add_shader_plane(plane)
    plane.set_shader_parameter_type("mousePos", "glUniform2f")
    plane.set_shader_parameter_type("shapeSize", "glUniform1f")
    plane.set_shader_parameter_type("mode", "glUniform1ui")
    plane.set_shader_parameter_type("noiseBits", "glUniform1uiv")
    plane.set_shader_parameter("noiseBits", len(NOISE_PATTERN), NOISE_PATTERN)


    if "--create-arrows" in config:
        global texture
        texture = render.TextureRect("../main/shaders/arrowr.png", "arrowr")
        texture.x, texture.y = 10*0.7, 5*0.7
        texture.scale_x = 5*0.7
        texture.scale_y = 5*0.7
        texture.z_index = 19

        buttons["scroll_r"] = render.Button(
           570,39,
            (25,62),
            (0.5, 0.5, 0.5, 1), PIXEL_SIZE, (0.8, 0.8, 0.8, 1),
            texture,
            rscroll,
            (0.6, 0.6, 0.6, 1),
            (0.8, 0.8, 0.8, 1),
            offsets_fix=-1,
        )
        buttons["scroll_r"].z_index = 8

        texture2 = render.TextureRect("../main/shaders/arrowl.png", "arrowl")
        texture2.x, texture2.y = 7*0.7, 5*0.7
        texture2.scale_x = 5*0.7
        texture2.scale_y = 5*0.7
        texture2.z_index = 19

        buttons["scroll_l"] = render.Button(
           30,39,
            (25,62),
            (0.5, 0.5, 0.5, 1), PIXEL_SIZE, (0.8, 0.8, 0.8, 1),
            texture2,
            lscroll,
            (0.6, 0.6, 0.6, 1),
            (0.8, 0.8, 0.8, 1),
            offsets_fix=-1,
        )
        buttons["scroll_l"].z_index = 8

    global pause_texture
    render.add_texture("../main/shaders/resume.png", "resume")
    pause_texture = render.TextureRect("../main/shaders/pause.png", "pause")
    pause_texture.z_index = 19
    pause_texture.x, pause_texture.y = 10,3
    pause_texture.scale_x, pause_texture.scale_y = 3.4,3.4
    buttons["pause_button"] = render.Button(
       990,118,
        (35,35),
        (0.5, 0.5, 0.5, 1), PIXEL_SIZE, (0.8, 0.8, 0.8, 1),
        pause_texture,
        pause_button,
        (0.6, 0.6, 0.6, 1),
        (0.8, 0.8, 0.8, 1),
        offsets_fix=-1,
    )
    buttons["pause_button"].z_index = 18




    brush_scroll = render.ScrollContainer(805,46-5-3,(800,100),17,"h")
    rect = render.ColorRect(805-5-1,46-5-6-3, (226,72), (0.5,0.5,0.5,1), PIXEL_SIZE*1.3, (0.8, 0.8, 0.8, 1), offsets_fix=-1)
    rect.z_index = 7
    #scroll.add_children(buttons["load"],buttons["save"],buttons["clear"])
    for i,name in enumerate(["circle_brush", "square_brush", "noise_brush"]):
        brush_texture = render.TextureRect(f"../main/shaders/{name}.png", name)
        brush_texture.x, brush_texture.y = 8,5
        brush_texture.scale_x, brush_texture.scale_y = 4,4
        brush_texture.z_index = 19
        button = render.Button(
        0,0,
        (60,60),
        (0.6,0.6,0.6,1), 0, (0,0,0,0),#PIXEL_SIZE*1.3
        brush_texture,
        brush_select,
        (0.7, 0.7, 0.7, 1),
        (0.6, 0.6, 0.3, 1),
        offsets_fix=0,
        )
        button.set_meta("brush_type", i+1)
        button.z_index = 8
        button.stay_pressed = True
        brush_scroll.add_child(button)
        if i+1 == 2:
            button.press()



    render.set_control_scale(1)


prev_brush = None
def brush_select(button):
    if button.press_state == render.PressState.JUST_PRESSED:
        global prev_brush
        if prev_brush is not None:
            prev_brush.reset()
            prev_brush.color = (0.6,0.6,0.6,1)
        global MODE
        prev_brush = button
        MODE = button.get_meta("brush_type")

pause_texture = None
is_paused: bool = False
def pause_button(button):
    if button.press_state == render.PressState.JUST_PRESSED:
        global is_paused
        is_paused = not is_paused
        if is_paused:
            chunk_manager.is_paused = True
            pause_texture.local_x = 5
            pause_texture.set_texture("resume")
        else:
            chunk_manager.is_paused = False
            pause_texture.local_x = 7
            pause_texture.set_texture("pause")




def rscroll(button):
    if button.press_state == render.PressState.PRESSED:
        scroll2.out_of_bounds_scroll_on = True
        variant.call_deferred(setattr, mainloop, "mouse_scroll_y", 1)
        #mainloop.mouse_scroll_y = 1

def lscroll(button):
    if button.press_state == render.PressState.PRESSED:
        scroll2.out_of_bounds_scroll_on = True
        variant.call_deferred(setattr, mainloop, "mouse_scroll_y", -1)
       # mainloop.mouse_scroll_y = -1

import tkinter as tk
from tkinter import filedialog

selected_button = None
prev_outline_color = None

def eraser_button(button):
    if button.press_state == render.PressState.JUST_PRESSED:# or (button.press_state == render.PressState.JUST_RELEASED and not button.held):
        global selected_button, prev_outline_color
        if not selected_button is None:# and (button != selected_button or selected_button.press_state == render.PressState.JUST_RELEASED):
            selected_button.reset()
            selected_button.label.color = (1, 1, 1, 1)
            selected_button.outline_color = prev_outline_color
        #if button.press_state == render.PressState.JUST_PRESSED:
            #print('FJFJ')
        mainloop.SELECTED_TYPE = 0
        selected_button = button
        button.label.color = (1, 1, 0.4, 1)
        prev_outline_color = button.outline_color
        button.outline_color = (1, 1, 0.2, 1)

def select(button):
    if button.press_state == render.PressState.JUST_PRESSED and button.x > scroll2.x - 80:
        global selected_button, prev_outline_color
        if not selected_button is None:
            selected_button.reset()
            selected_button.label.color = (1, 1, 1, 1)
            selected_button.outline_color = prev_outline_color
        selected_button = button
        button.label.color = (1, 1, 0.4, 1)
        prev_outline_color = button.outline_color
        button.outline_color = (1, 1, 0.2, 1)
        mainloop.SELECTED_TYPE = button.get_meta("type")

def clear_button(button):
    if button.press_state == render.PressState.JUST_PRESSED:
        call_deferred(chunk_manager.clear_all)



import lzma
def save_button(button):
    if button.press_state != render.PressState.JUST_PRESSED: return
    def save_deferred(path):
        try:
            with open(path, "wb") as file:
                snapshot = chunk_manager.make_snapshot()
                file.write(lzma.compress(snapshot))
        except:
            pass

    root = tk.Tk(); root.withdraw()
    path = filedialog.asksaveasfilename(
        title="Save as",
        initialfile="save.pysand",
        defaultextension=".pysand",
        filetypes=(("Pysand files", "*.pysand"), ("All files", "*.*"))
    )
    root.destroy()

    variant.call_deferred(save_deferred, path)

def load_button(button):
    if button.press_state != render.PressState.JUST_PRESSED: return

    root = tk.Tk(); root.withdraw()
    path = filedialog.askopenfilename(
        title="Load save",
        defaultextension=".pysand",
        filetypes=(("Pysand files", "*.pysand"), ("All files", "*.*"))
    )
    root.destroy()
    if not os.path.exists(path): return

    snapshot = lzma.decompress(open(path, "rb").read())
    call_deferred(chunk_manager.apply_snapshot,snapshot)


fps_log: list[int] = []
window_size = 5

WINDOW_HEIGHT = None
WINDOW_WIDTH = None

def fps(delta:float):
    current_fps = 1000
    if delta != 0: current_fps = 1/delta
    fps_log.append(current_fps)
    if len(fps_log) > window_size:
        fps_log.pop(0)
    if chunk_manager.update_tick:
        label.text = str(int(sum(fps_log) / len(fps_log)))
      #  label.text = str(int(min(fps_log)))


_float_pen_size = 2.0
pen_size = 2
MODE = 2


prev_pos = None
import math

def pen_get_random() -> int:
    return 1 if randint(0,10) > 7 else 0

# mx = x % 12;
# my = y % 12;
# idx = my * 12 + mx;
NOISE_PATTERN = [pen_get_random() for _ in range(12*12)]
PEN_UPDATE_FREQ = 0.3
pen_uses = PEN_UPDATE_FREQ
def pen(delta:float):
    global prev_pos, pen_uses, pen_size
    update_pattern = False
    if pen_uses > PEN_UPDATE_FREQ:
        update_pattern = True; pen_uses = 0.0


    screen_pos = mainloop.screen_mouse_position
    global_pos = Vector2((screen_pos[0]+1.333) / mainloop.PIXEL_SIZE, (WINDOW_HEIGHT - screen_pos[1] + 1.333) / mainloop.PIXEL_SIZE, i=True)
    global MODE, _float_pen_size
    # - 1.4*PIXEL_SIZE,oy - 1.1*PIXEL_SIZE,

    display_pos = Vector2(screen_pos[0], (WINDOW_HEIGHT - screen_pos[1]), i=True)
    plane.set_shader_parameter("mousePos",
    display_pos.x,
    display_pos.y)
    plane.set_shader_parameter("shapeSize", pen_size)
    plane.set_shader_parameter("mode", MODE)
    #if chunk_manager.get_chunk(int(global_pos.x), int(global_pos.y), None) is None: return
    #hover.x, hover.y = math.floor(display_pos.x / PIXEL_SIZE) * PIXEL_SIZE - 0.4*PIXEL_SIZE, math.floor(display_pos.y / PIXEL_SIZE) * PIXEL_SIZE - 0.3*PIXEL_SIZE

    _float_pen_size += mainloop.mouse_scroll_y * 0.6
    _float_pen_size = variant.clamp(_float_pen_size, 0, 6)
    pen_size = int(_float_pen_size)
    NOISE_PATTERN[(pen_size % 12) + (pen_size % 12) * 12] = 1

    if mainloop.mouse_pressed and display_pos.y > rect2.y:
        pen_uses += delta
        visited = set([])
        length = max(1, global_pos.distance_to(prev_pos))
        row_size = (2*pen_size + 1)
        if update_pattern:
            plane.set_shader_parameter("noiseBits", len(NOISE_PATTERN), NOISE_PATTERN)

        def draw_here(i):
            ox, oy = i / length * (global_pos.x - prev_pos.x) + prev_pos.x, i / length * (global_pos.y - prev_pos.y) + prev_pos.y

            for j in range(row_size*row_size):
                x, y = j % row_size - pen_size, j // row_size - pen_size

                if (MODE == 1 or MODE == 3) and (x**2 + y**2) > pen_size**2: continue
                if (ox+x, oy+y) in visited: continue
                if MODE == 3:
                    idx = ((x+pen_size) % 12) + ((y+pen_size) % 12) * 12
                    if (x,y) == (0,0): NOISE_PATTERN[idx] = 2
                    prev = NOISE_PATTERN[idx]
                    if update_pattern:
                        NOISE_PATTERN[idx] = pen_get_random() if not (x,y) == (0,0) else 1

                    if prev == 0: continue

                visited.add((ox+x,oy+y))
                chunk_manager.global_set_cell(int(ox+x),int(oy+y),mainloop.SELECTED_TYPE)

        if MODE != 3:
            for i in range(int(length)):
                draw_here(i)
        else:
            draw_here(int(length)-1)


    prev_pos = global_pos



def _process(delta:float) -> None:
    fps(delta)
    pen(delta)