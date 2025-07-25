import pickle
from multiprocessing import shared_memory, Manager
import numpy as np
import ui

USE_DEBUG = False
USE_MODULES = ["element_storage", "render", "mainloop"]


CHUNK_SIZE = 12
UPDATES_PER_SECOND = 60
RENDERS_PER_SECOND = 60
MAX_UPDATE_INTENSITY = 1.0
WINDOW_WIDTH = None
WINDOW_HEIGHT = None
PEN_SIZE = 6

element_storage = None
mainloop = None
render = None
variant = None

DATA_LEN: int = CHUNK_SIZE * CHUNK_SIZE

is_in_bounds = lambda x, y: (x // CHUNK_SIZE, y // CHUNK_SIZE) in chunks

is_paused: bool = False

PIXEL_SIZE = None
from array import array

class Chunk:
    was_updated: bool = False
    skipped_over_count: int = 0
    neighbors_kept_alive: bool = False
    #element_processor: "ElementProcessor" = None
    update_intensity: float = 0.0

    local_is_in_bounds = lambda self, x, y: 0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE


    def _loaded_init(self):
        pass
        # self.rect = render.ColorRect(
        #     self.xo * CHUNK_SIZE * PIXEL_SIZE, self.yo * CHUNK_SIZE * PIXEL_SIZE,
        #     (CHUNK_SIZE * PIXEL_SIZE, CHUNK_SIZE * PIXEL_SIZE),
        #     (1, 0, 0, 0.0), 0, (1, 1, 1, 1)
        # )



    def __init__(self, xo: int, yo: int):
        self.data = array("L", [0]*(CHUNK_SIZE*CHUNK_SIZE))
        self.first_assign = False
        self.force_update = False

        self.xo, self.yo = xo, yo
        #self.data = np.zeros((CHUNK_SIZE, CHUNK_SIZE), dtype=np.uint8)
        self.prev = array("L", [0]*(CHUNK_SIZE*CHUNK_SIZE))#np.zeros_like(self.data)

        self.even_tick = False
        self.render_chunk = render.add_chunk(xo, yo, self.data)
        self.visited = set([])
        self.merge_visited = set([])
        self.is_uniform = False
        self.tick_modulus = [True, True] + [False]*5

        # self.rect = render.ColorRect(
        #     self.xo * CHUNK_SIZE * PIXEL_SIZE, self.yo * CHUNK_SIZE * PIXEL_SIZE,
        #     (CHUNK_SIZE * PIXEL_SIZE, CHUNK_SIZE * PIXEL_SIZE),
        #     (1, 0, 0, 0.0), 0, (1, 1, 1, 1)
        # )


    def decrement_update(self):
        self.update_intensity -= update_delta * 16
        if 0 < self.update_intensity < 0.03:
            self.update_intensity = 0.0

    def update_ended(self):
        self.neighbors_kept_alive = False
        self.was_updated = False
        self.skipped_over_count = 0
        self.visited.clear()
        self.prev = self.data
        self.first_assign = True


    def keep_alive(self, and_neighbours: bool = False):
        if is_paused:
            to_render.add(self)
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

    def get_bit_state(self, x: int, y: int):
        if self.local_is_in_bounds(x, y):
            return self.prev[y*CHUNK_SIZE+x] & 0xFF
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if target is None:
            return 0
        #ly, lx = gy % CHUNK_SIZE, gx % CHUNK_SIZE
        return target.prev[(gy % CHUNK_SIZE)*CHUNK_SIZE + gx % CHUNK_SIZE] & 0xFF

    def set_bit_state(self, x: int, y: int, val: int):
        if self.local_is_in_bounds(x, y):
            self.data[y*CHUNK_SIZE+x] = (self.data[y*CHUNK_SIZE+x] & 0xFF00) | (val & 0xFF)
            return True
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if target is None:
            return False
        local_x, local_y = gx % CHUNK_SIZE, gy % CHUNK_SIZE
        target.data[local_y*CHUNK_SIZE+local_x] = (target.data[local_y*CHUNK_SIZE+local_x] & 0xFF00) | (val & 0xFF)

        return True

    def get_cell(self, x: int, y: int) -> int:
        if self.local_is_in_bounds(x, y):
            return self.prev[y*CHUNK_SIZE+x] >> 8# if not (x,y) in self.visited else self.visited[(x,y)]

        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if target is None:
            return 99
        #ly, lx = gy % CHUNK_SIZE, gx % CHUNK_SIZE
        return target.prev[(gy % CHUNK_SIZE)*CHUNK_SIZE + gx % CHUNK_SIZE] >> 8# if target.was_updated else target.data[ly, lx]#if not (lx,ly) in target.visited else target.visited[(lx,ly)]

    def move_cell(self, ox: int, oy: int, x: int, y: int, v: int):
        if not self.is_visited(x,y):
            self.set_cell(ox,oy, self.get_cell(x,y))
            self.set_cell(x,y,v)

    def get_chunk(self, x: int, y: int):
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        chunk = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        return chunk if not chunk is None else dummy_chunk

    def is_visited(self, x: int, y: int):
        if 0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE: return (x,y) in self.visited
        gx, gy = x + CHUNK_SIZE * self.xo, y + CHUNK_SIZE * self.yo
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if not target: return True
        return (gx % CHUNK_SIZE, gy % CHUNK_SIZE) in target.visited

    def skip_over(self):
        self.skipped_over_count += 1

    def unskip(self):
        self.skipped_over_count -= 1



    def set_cell(self, x: int, y: int, val: int) -> bool:
        # if self.is_visited(x,y):
        #     return False
        self.visited.add((x, y))
        if self.local_is_in_bounds(x, y):
            self.is_uniform = False
            #if not (x,y) in self.visited:
            self.data[y*CHUNK_SIZE+x] = val * 256
           # print(self.data)
            self.keep_alive()
            self.is_uniform = False
            self.first_assign = False
            return True
        gx, gy = self.xo * CHUNK_SIZE + x, self.yo * CHUNK_SIZE + y
        target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
        if target is None:
            return False
        local_x, local_y = gx % CHUNK_SIZE, gy % CHUNK_SIZE
        target.keep_alive()

        target.visited.add((local_x, local_y))
        target.data[local_y*CHUNK_SIZE+local_x] = val * 256

        target.is_uniform = False
        target.first_assign = False

        return True

   # get_cell = lambda self,x,y: self.prev[y,x] if (0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE) else chunks.get(((self.xo*CHUNK_SIZE+x) // CHUNK_SIZE, (self.yo*CHUNK_SIZE+y) // CHUNK_SIZE), dummy_chunk).prev[y % CHUNK_SIZE, x % CHUNK_SIZE]

    iter_regular = range(CHUNK_SIZE)
    iter_uniform = [0, CHUNK_SIZE-1]

    def update(self):
        self.ticks = ticks
        self.was_updated = True

        self.even_tick = ticks % 2 == 0
        self.skipped_over_count = 0
        self.prev = array("L", self.data)

        assign_is_uniform = self.first_assign
        first = self.prev[0]

        for i in range(5):
            i += 2
            self.tick_modulus[i] = ticks % i == True

        total_iters = 0
        for x in Chunk.iter_regular:
            x = x if ticks % 2 == 0 else CHUNK_SIZE-x-1
            curr_range = Chunk.iter_regular if not self.is_uniform or x == 0 or x == CHUNK_SIZE-1 else Chunk.iter_uniform
            for y in curr_range:
                total_iters += 1
                if (x,y) in self.visited:
                    assign_is_uniform = False
                    continue
                current = self.prev[y*CHUNK_SIZE+x]# >> 8
                if current != first:
                    assign_is_uniform = False

                #if self.is_uniform and 0 < x < CHUNK_SIZE-1 and 0 < y < CHUNK_SIZE-1:
                #   self.skip_over(); continue

                if current in element_storage.element_calls:
                    curr_bit = 0
                    #if element_storage.update_types[current].is_plant:
                   #     curr_bit = current & 0xFF
                    element_storage.element_calls[current](self, current, curr_bit, x, y)
                else:
                    self.skipped_over_count += 1
        #

        if self.is_uniform:
            self.skipped_over_count += CHUNK_SIZE ** 2 - total_iters

        if self.skipped_over_count >= CHUNK_SIZE ** 2:
            self.decrement_update()


        self.is_uniform = assign_is_uniform
        #self.prev = self.data

    def render(self):
        self.render_chunk.update(self.data)


def clear_all():
    for c in chunks:
        for i in range(len(chunks[c].data)):
            chunks[c].data[i] = 0
        chunks[c].keep_alive()


def make_snapshot() -> bytearray:
    return pickle.dumps(chunks)


def apply_snapshot(snapshot: bytearray):

    global chunks
    new_chunks = pickle.loads(snapshot)
    for c in new_chunks:
        chunks[(int(c[0]), int(c[1]))] = new_chunks[c]
    for c in chunks:
        chunks[c].keep_alive()
        chunks[c].render_chunk = render.add_chunk(*c, chunks[c].data)
        #chunks[c]._loaded_init()





class DummyChunk:
    def __init__(self):
        self.data = array("L", [99 * 256]*(CHUNK_SIZE*CHUNK_SIZE))
        self.prev = array("L", [99 * 256]*(CHUNK_SIZE*CHUNK_SIZE))
        self.visited = set([])
        self.first_assign = False
        self.was_updated = False
        self.is_uniform = False
       # self.merge_
        self.update_intensity = 0
    def mark_dirty(self, x:int, y:int):
        pass
    def unskip(self):
        pass
    def keep_alive(self, and_neighbors: bool = False):

        pass


def global_set_cell(gx: int, gy: int, v: int, bit_value = False):
    target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE))
    if target:
       # target.force_border.add((gx % CHUNK_SIZE, gy % CHUNK_SIZE))
        target.is_uniform = False
        target.keep_alive()
        target.data[(gy % CHUNK_SIZE) * CHUNK_SIZE + gx % CHUNK_SIZE] = v * 256 if not bit_value else v


dummy_chunk = DummyChunk()


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
ticks = 0
CHUNKS_RECT = None

def _ready() -> None:
    for x in range(CHUNKS_RECT[0],CHUNKS_RECT[2]):
        for y in range(CHUNKS_RECT[1],CHUNKS_RECT[3]):
            chunks[(x, y)] = Chunk(x, y)



def _process(delta: float) -> None:
    global render_timestamp, timestamp, update_delta, update_tick
    dummy_chunk.visited.clear()
    #dummy_chunk.merge_.clear()

    if mainloop.time_passed - timestamp > 1 / UPDATES_PER_SECOND:
        global ticks
        update_delta = mainloop.time_passed - timestamp
        timestamp = mainloop.time_passed
        update_tick = True
        ticks += 1
        element_storage.clear()
        if not is_paused:
            for c in chunks.values():
                if c.is_alive():
                    c.update()
                    to_render.add(c)
                #     if not c.is_uniform:
                #         c.rect.color[0], c.rect.color[1] = 1, 0
                #     else:
                #         c.rect.color[0], c.rect.color[1] = 0, 1
                #     c.rect.color[3] = 0.3
                # else:
                #     c.rect.color[3] = 0.0
        #dummy_chunk.data, dummy_chunk.prev = dummy_chunk.prev, dummy_chunk.data

        for c in chunks.values():
            c.update_ended()
    else:
        update_tick = False
    if mainloop.time_passed - render_timestamp > 1 / RENDERS_PER_SECOND:
        render_timestamp = mainloop.time_passed
        for chunk in to_render:
            chunk.render()
        to_render.clear()
