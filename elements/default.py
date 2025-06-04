from random import randint

chunk_manager = None
element_storage = None
element_processor = None
get_cell = None
CELL_INDEX: int = 1

def update(chunk, x: int, y: int):
    bottom = chunk.get_cell(x,y-1)
    do_skip_over = True

    if bottom in element_storage.soft:
        do_skip_over = False
        if chunk.set_cell(x,y - 1,1):
            chunk.set_cell(x, y, bottom)
        chunk.unskip()
        chunk.keep_alive(and_neighbours=True)
    else:
        left = chunk.get_cell(x - 1,y - 1)
        if left in element_storage.soft:
            do_skip_over = False
            if randint(0,10) > 6:
                if chunk.set_cell(x - 1, y - 1, 1):
                    chunk.set_cell(x,y,left)
            chunk.unskip()
            chunk.keep_alive(and_neighbours=True)

        else:
            right = chunk.get_cell(x + 1,y - 1)
            if right in element_storage.soft:
                do_skip_over = False
                if randint(0, 10) > 6:
                    if chunk.set_cell(x + 1, y - 1, 1):
                        chunk.set_cell(x, y, right)
                chunk.unskip()
                chunk.keep_alive(and_neighbours=True)

    if do_skip_over:
        chunk.skip_over()