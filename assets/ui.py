import os.path

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

buttons = {}
def _ready() -> None:
    global label
    global prev_pos
    prev_pos = Vector2(0, 0, i=True)
    label = render.Label("hello",120*5,10*5,(1,1), (1,0,0,1))
    ox, oy = CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[0], CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[1]

    rect2 = render.ColorRect(
        ox - 1.4*PIXEL_SIZE,oy - 1.1*PIXEL_SIZE,
        (CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[2] - ox + 2*PIXEL_SIZE, CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[3] + PIXEL_SIZE*0.4 + 0.4*PIXEL_SIZE - oy),
        (0,1,0,0),PIXEL_SIZE,(1,1,1,1),offsets_fix=1
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


    scroll = render.ScrollContainer(85,121,(100,100),10,"h")
    scroll.smooth_scroll = True
    scroll.smooth_scroll_speed = 20.0
    scroll.add_children(buttons["load"],buttons["save"],buttons["clear"])

    render.set_control_scale(1)

import tkinter as tk
from tkinter import filedialog
def clear_button(button):
    if button.press_state == render.PressState.JUST_PRESSED:
        chunk_manager.clear_all()



def save_button(button):
    if button.press_state != render.PressState.JUST_PRESSED: return

    root = tk.Tk(); root.withdraw()
    path = filedialog.asksaveasfilename(
        title="Save as",
        initialfile="save.pysand",
        defaultextension=".pysand",
        filetypes=(("Pysand files", "*.pysand"), ("All files", "*.*"))
    )
    root.destroy()

    try:
        with open(path, "wb") as file:
            snapshot = chunk_manager.make_snapshot()
            file.write(snapshot)
    except:
        pass

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

    snapshot = open(path, "rb").read()
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



PEN_SIZE = 3


prev_pos = None
def pen(delta:float):
    global prev_pos
    screen_pos = mainloop.screen_mouse_position
    global_pos = Vector2(screen_pos[0] / mainloop.PIXEL_SIZE, (WINDOW_HEIGHT - screen_pos[1]) / mainloop.PIXEL_SIZE, i=True)
    if mainloop.mouse_pressed:
        prev_pressed = True
        visited = set([])
        length = max(1, global_pos.distance_to(prev_pos))

        for i in range(int(length)):
            ox, oy = i / length * (global_pos.x - prev_pos.x) + prev_pos.x, i / length * (global_pos.y - prev_pos.y) + prev_pos.y
            for j in range(PEN_SIZE*PEN_SIZE):
                x, y = j % PEN_SIZE - PEN_SIZE // 2, j // PEN_SIZE - PEN_SIZE // 2
                if (ox+x, oy+y) in visited: continue
                visited.add((ox+x,oy+y))
                chunk_manager.global_set_cell(int(ox+x),int(oy+y),mainloop.SELECTED_TYPE)
    prev_pos = global_pos


def _process(delta:float) -> None:
    fps(delta)
    pen(delta)