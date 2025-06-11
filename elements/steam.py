from random import randint

chunk_manager = None
element_processor = None
get_cell = None
CELL_INDEX: int = 6
visited: dict[tuple[int,int]: set[tuple[int, int]]] = {}

def clear(c: tuple[int,int]):
    visited.clear()


def update(chunk, x: int, y: int):
    do_skip_over: bool = True
   # pos = (x,y)
   # keep_alive_list = ((x - 1, y), (x, y), (x + 1, y))
    top = chunk.get_cell(x, y + 1)
    if top not in element_storage.gases and randint(0,10000) > 9996 and not chunk.is_visited(x,y):
        chunk.keep_alive()
        chunk.set_cell(x,y,2)
        return

    if top == 0 and not chunk.is_visited(x,y+1):
        if chunk.set_cell(x, y + 1, 6):
            do_skip_over = False
            chunk.set_cell(x, y, 0)
       #     pos = (x, y - 1)
            # chunk.keep_alive()
            # chunk.unskip()
    else:
        left = chunk.get_cell(x - 1, y) if not chunk.is_visited(x - 1, y) else 9
        right = chunk.get_cell(x + 1, y) if not chunk.is_visited(x + 1, y) else 9

        if left == 0 and right == 0:
            do_skip_over = False
            add = 1 if randint(0, 10) > 4 else -1
            if add == -1:
                if left == 0 and randint(0, 10) > 4:
                    if chunk.set_cell(x + add, y, 6):
                        chunk.set_cell(x, y, 0)
            else:
                if right == 0 and randint(0, 10) > 4:
                    if chunk.set_cell(x + add, y, 6):
                        chunk.set_cell(x, y, 0)
                #  pos = (x + add, y)
            # chunk.keep_alive()
            # chunk.unskip()
        elif left == 0:
            do_skip_over = False
            add = -1
            if left == 0 and randint(0, 10) > 4:
                if chunk.set_cell(x + add, y, 6):
                    chunk.set_cell(x, y, 0)

        elif right == 0:
            do_skip_over = False
            add = 1
            if right == 0 and randint(0, 10) > 4:
                if chunk.set_cell(x + add, y, 6):
                    chunk.set_cell(x, y, 0)

    if do_skip_over:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
    #else:
    #    chunk.keep_alive()