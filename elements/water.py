from random import randint

chunk_manager = None
element_processor = None
get_cell = None
CELL_INDEX: int = 2

def update(chunk, x: int, y: int):
    do_skip_over: bool = True
    if chunk.get_cell(x, y - 1) == 0:
        if chunk.set_cell(x, y - 1, 2):
            do_skip_over = False
            chunk.set_cell(x, y, 0)
            chunk.keep_alive(and_neighbours=True)
            chunk.unskip()
    else:
        left = chunk.get_cell(x-1, y)
        right = chunk.get_cell(x+1, y)

        if left == 0 and right == 0:
            do_skip_over = False
            add = 1 if randint(0, 10) > 4 else -1
            if randint(0,10) > 4:
                if chunk.set_cell(x + add, y, 2):
                    chunk.set_cell(x, y, 0)
            chunk.keep_alive(and_neighbours=True)
            chunk.unskip()
        elif left == 0:
            do_skip_over = False
            add = -1
            if randint(0,10) > 4:
                if chunk.set_cell(x + add, y, 2):
                    chunk.set_cell(x, y, 0)
            chunk.keep_alive(and_neighbours=True)
            chunk.unskip()
        elif right == 0:
            do_skip_over = False
            add = 1
            if randint(0, 10) > 4:
                if chunk.set_cell(x + add, y, 2):
                    chunk.set_cell(x, y, 0)
            chunk.keep_alive(and_neighbours=True)
            chunk.unskip()

    if do_skip_over:
        chunk.skip_over()
    #else:
    #    chunk.keep_alive()