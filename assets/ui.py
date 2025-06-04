TAGS = []
USE_MODULES = ["render", "mainloop", "chunk_manager", "*variant"]
chunk_manager = None
render = None
mainloop = None
CHUNKS_RECT = None
PIXEL_SIZE = None
CHUNK_SIZE = None

label = None
modules_dict = {}
def _ready() -> None:
    global label
    global prev_pos
    prev_pos = Vector2(0, 0, i=True)
    label = render.Label("hello",120*5,10*5,(1,1), (1,0,0,1))
    ox, oy = CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[0], CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[1]
    # rect = render.ColorRect(
    #     ox - 1.4*PIXEL_SIZE - PIXEL_SIZE,oy - 0.5*PIXEL_SIZE - PIXEL_SIZE,
    #     (CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[2] - ox + 2*PIXEL_SIZE, CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[3] - oy),
    #     (0,1,0,0),PIXEL_SIZE,(0.5,0.5,0.5,1)
    # )
    rect2 = render.ColorRect(
        ox - 1.4*PIXEL_SIZE,oy - 0.5*PIXEL_SIZE,
        (CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[2] - ox + 2*PIXEL_SIZE, CHUNK_SIZE * PIXEL_SIZE * CHUNKS_RECT[3] - oy),
        (0,1,0,0),PIXEL_SIZE,(1,1,1,1),offsets_fix=1
    )

    rect2 = render.Button(
        40,30,
        (100,35),
        (0.5,0.5,0.5,1),PIXEL_SIZE,(0.8,0.8,0.8,1),
        render.Label("CLEAR",4,5,(1,1), (1,1,1,1)),
        testcall,
        (0.6, 0.6, 0.6, 1),
        (0.8, 0.8, 0.8, 1),
        offsets_fix=-1,
    )

def testcall(button):
    if button.press_state == render.PressState.JUST_PRESSED:
        for i in chunk_manager.chunks:
            chunk_manager.chunks[i].data.fill(0)
            chunk_manager.chunks[i].keep_alive()

fps_log: list[int] = []
window_size = 5

CHUNK_SIZE = None
PIXEL_SIZE = None
WINDOW_HEIGHT = None
WINDOW_WIDTH = None

def fps(delta:float):
    current_fps = 1000
    if delta != 0: current_fps = 1/delta
    fps_log.append(current_fps)
    if len(fps_log) > window_size:
        fps_log.pop(0)
    if mainloop.ticks % 120 == 0:
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