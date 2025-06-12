from random import randint

chunk_manager = None
element_processor = None
get_cell = None
CELL_INDEX: int = 2
visited: dict[tuple[int,int]: set[tuple[int, int]]] = {}

def clear(c: tuple[int,int]):
    visited.clear()


def update(chunk, x: int, y: int):
    do_skip_over: bool = True
    chunk.visited.add((x,y))
   # pos = (x,y)
   # keep_alive_list = ((x - 1, y), (x, y), (x + 1, y))

    bot = chunk.get_cell(x, y - 1)
    if bot in element_storage.gases and not chunk.is_visited(x,y-1):
        chunk.set_cell(x, y-1, 2)
        chunk.set_cell(x, y, bot)
        chunk.keep_alive(and_neighbours=True)
        return
    if bot == 5:
        chunk.set_cell(x, y, 6)
        chunk.keep_alive()
        return
    if bot == 0:
        if not chunk.is_visited(x,y-1) and chunk.set_cell(x, y - 1, 2) :
            chunk.set_cell(x, y, 0)
        do_skip_over = False
       #     pos = (x, y - 1)
            # chunk.keep_alive()
            # chunk.unskip()
    else:
        left = chunk.get_cell(x-1, y) if not chunk.is_visited(x-1,y) else 9
        right = chunk.get_cell(x+1, y) if not chunk.is_visited(x+1,y) else 9

        if left in element_storage.gases and right in element_storage.gases:
            do_skip_over = False
            add = 1 if randint(0, 10) > 4 else -1
            if add == -1:
                if left in element_storage.gases and randint(0,10) > 2:
                    if chunk.set_cell(x + add, y, 2):
                        chunk.set_cell(x, y, left)
            else:
                if right in element_storage.gases and randint(0,10) > 2:
                    if chunk.set_cell(x + add, y, 2):
                        chunk.set_cell(x, y, right)
                  #  pos = (x + add, y)
            # chunk.keep_alive()
            # chunk.unskip()
        elif left in element_storage.gases:
            do_skip_over = False
            add = -1
            if left == 0 and randint(0, 10) > 2:
                if chunk.set_cell(x + add, y, 2):
                    chunk.set_cell(x, y, left)

        elif right in element_storage.gases:
            do_skip_over = False
            add = 1
            if right == 0 and randint(0, 10) > 2:
                if chunk.set_cell(x + add, y, 2):
                    chunk.set_cell(x, y, right)

    if do_skip_over:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
    #else:
    #    chunk.keep_alive()