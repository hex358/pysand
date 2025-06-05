from multiprocessing import shared_memory, Manager
import numpy as np

USE_MODULES = ["element_storage", "render", "mainloop"]

CHUNK_SIZE = 16
UPDATES_PER_SECOND = 60
RENDERS_PER_SECOND = 60
MAX_UPDATE_INTENSITY = 3.0
WINDOW_WIDTH = None
WINDOW_HEIGHT = None
PEN_SIZE = 6

element_storage = None
mainloop = None
render = None
variant = None

empty = np.zeros((CHUNK_SIZE, CHUNK_SIZE), dtype=np.uint8)
DATA_LEN: int = CHUNK_SIZE * CHUNK_SIZE

is_in_bounds = lambda x, y: (x // CHUNK_SIZE, y // CHUNK_SIZE) in chunks

PIXEL_SIZE = None
class Chunk:
    was_updated: bool = False
    skipped_over_count: int = 0
    neighbors_kept_alive: bool = False
    #element_processor: "ElementProcessor" = None
    update_intensity: float = 0.0

    local_is_in_bounds = lambda self, x, y: 0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE



    def __init__(self, xo: int, yo: int):
        #self.element_processor = element_storage.create_element_processor(chunk=self)
        self.xo, self.yo = xo, yo
        self.data = np.ndarray((CHUNK_SIZE, CHUNK_SIZE), dtype=np.uint8)
        self.data.fill(0)
        # self.data_swap = np.ndarray((CHUNK_SIZE, CHUNK_SIZE), dtype=np.uint8)
        # self.data_swap.fill(0)
        #self.to_swap: list[tuple[int, int, int]] = []
        self.render_chunk = render.add_chunk(xo, yo, self.data)
        self.visited = {}
        self.merge_visited = {}
        # self.rect = render.ColorRect(
        # xo*CHUNK_SIZE*PIXEL_SIZE,yo*CHUNK_SIZE*PIXEL_SIZE,
        # (CHUNK_SIZE*PIXEL_SIZE,CHUNK_SIZE*PIXEL_SIZE),
        # (1,0,0,0.4),0,(1,1,1,1)
 #   )

    def decrement_update(self):
        self.update_intensity -= update_delta
        if 0 < self.update_intensity < 0.03:
            self.update_intensity = 0.0

    def update_ended(self):
        self.neighbors_kept_alive = False
        self.was_updated = False
        self.skipped_over_count = 0

    def keep_alive(self, and_neighbours: bool = False):
        self.update_intensity = MAX_UPDATE_INTENSITY
        if and_neighbours and not self.neighbors_kept_alive:
            self.neighbors_kept_alive = True
            xo, yo = self.xo, self.yo
            get_chunk(xo - 1, yo).keep_alive(); get_chunk(xo, yo - 1).keep_alive()
            get_chunk(xo, yo + 1).keep_alive(); get_chunk(xo + 1, yo).keep_alive()
            get_chunk(xo + 1, yo + 1).keep_alive(); get_chunk(xo + 1, yo - 1).keep_alive()
            get_chunk(xo - 1, yo - 1).keep_alive(); get_chunk(xo - 1, yo + 1).keep_alive()

    def to_global(self, x: int = None, y: int = None):
        if x is not None and y is not None:
            return self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        if x is not None:
            return self.xo * CHUNK_SIZE + x
        if y is not None:
            return self.yo * CHUNK_SIZE + y

    def is_alive(self) -> bool:
        return self.update_intensity > 0.03

    def get_cell(self, x: int, y: int) -> int:
        if self.local_is_in_bounds(x, y):
            return self.data[y, x] if not (x,y) in self.visited else self.visited[(x,y)]
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if target is None:
            return 9
        ly, lx = gy % CHUNK_SIZE, gx % CHUNK_SIZE
        return target.data[ly, lx] if not (lx,ly) in target.visited else target.visited[(lx,ly)]

    def get_chunk(self, x: int, y: int):
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        chunk = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        return chunk if not chunk is None else dummy_chunk

    def skip_over(self):
        self.skipped_over_count += 1

    def unskip(self):
        self.skipped_over_count -= 1

    def set_cell(self, x: int, y: int, val: int) -> bool:
        if self.local_is_in_bounds(x, y):
            self.data[y, x] = val
            if not (x,y) in self.visited:
                self.visited[(x, y)] = val
            self.keep_alive()
            return True
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if target is None:
            return False
        local_x, local_y = gx % CHUNK_SIZE, gy % CHUNK_SIZE
        target.keep_alive()
        if target.was_updated:
            target.data[local_y, local_x] = val
        else:
            if not (local_x, local_y) in target.merge_visited:
                target.merge_visited[(local_x, local_y)] = val
            target.data[local_y, local_x] = val
        return True

    def update(self):
        self.was_updated = True

        self.skipped_over_count = 0
        self.visited = {**self.merge_visited}
        self.merge_visited.clear()

        for x in range(CHUNK_SIZE):
            for y in range(CHUNK_SIZE):
                if (x,y) in self.visited: continue
                current = self.get_cell(x,y)
                if not current in element_storage.skip:
                    element_storage.element_calls[current](self, x, y)
                else:
                    self.skip_over()
        if self.skipped_over_count >= CHUNK_SIZE * CHUNK_SIZE:
            self.update_intensity = 0.0

    def render(self):
        self.render_chunk.update(self.data)


def clear_all():
    for i in chunks:
        chunks[i].data.fill(0)
        chunks[i].keep_alive()



def make_snapshot() -> bytearray:
    buff = bytearray()
    for c in chunks:
        ints = bytearray()
        buff.append(chunks[c].xo); buff.append(chunks[c].yo)
        for i in range(CHUNK_SIZE * CHUNK_SIZE):
            ints.append(chunks[c].data[i // CHUNK_SIZE, i % CHUNK_SIZE])
        buff.extend(ints)
    return buff


def apply_snapshot(snapshot: bytearray):
    #chunks.clear()
    shape = (CHUNK_SIZE, CHUNK_SIZE)
    stack = {"xo": 0, "yo": 0, "array": np.ndarray(shape,dtype=np.uint8)}

    for i in range(len(snapshot)):
        caret = i % (CHUNK_SIZE * CHUNK_SIZE + 2)
        if caret == 0 and i > 0:
            chunk = chunks.setdefault((stack["xo"], stack["yo"]), Chunk(stack["xo"], stack["yo"]))
            chunk.data = stack["array"]; stack["array"] = np.zeros_like(stack["array"])
            chunks[(stack["xo"], stack["yo"])] = chunk; chunk.keep_alive()
        if caret == 0: stack["xo"] = snapshot[i]
        if caret == 1: stack["yo"] = snapshot[i];
        if caret > 1:
            caret -= 2
            stack["array"][caret // CHUNK_SIZE, caret % CHUNK_SIZE] = snapshot[i]




class DummyChunk:
    def mark_dirty(self, x:int, y:int):
        pass
    def unskip(self):
        pass
    def keep_alive(self, and_neighbors: bool = False):
        pass


def global_set_cell(gx: int, gy: int, v: int):
    target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
    if target:
        target.keep_alive()
        target.data[gy % CHUNK_SIZE, gx % CHUNK_SIZE] = v


dummy_chunk = DummyChunk()

def get_cell(gx: int, gy: int):
    target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
    if target is None:
        return 9
    return target.data[gy % CHUNK_SIZE, gx % CHUNK_SIZE]

def get_chunk(xo: int, yo: int, default=dummy_chunk) -> Chunk:
    return chunks.get((xo, yo), default)

chunks: dict[tuple[int, int], Chunk] = {}
modules_dict = {}

manager: Manager = None
a: int = 0
timestamp: float = 0.0
render_timestamp: float = 0.0
update_delta: float = 0.0
prev_len = 0
to_render: set[Chunk] = set([])
update_tick: bool = False
update_calls = None
CHUNKS_RECT = None

def _ready() -> None:
    global manager
    manager = Manager()
    for x in range(CHUNKS_RECT[0],CHUNKS_RECT[2]):
        for y in range(CHUNKS_RECT[1],CHUNKS_RECT[3]):
            chunks[(x, y)] = Chunk(x, y)

def _process(delta: float) -> None:
    global render_timestamp, timestamp, update_delta, update_tick

    if mainloop.time_passed - timestamp > 1 / UPDATES_PER_SECOND:
        update_delta = mainloop.time_passed - timestamp
        timestamp = mainloop.time_passed
        update_tick = True
        for c in chunks.values():
            if c.is_alive():
                c.update()
              #  c.rect.color[3] = 0.5
                to_render.add(c)
           # else:
           #     c.rect.color[3] = 0.0
        for c in chunks.values():
            c.update_ended()
    else:
        update_tick = False
    if mainloop.time_passed - render_timestamp > 1 / RENDERS_PER_SECOND:
        render_timestamp = mainloop.time_passed
        for chunk in to_render:
            chunk.render()
        to_render.clear()
