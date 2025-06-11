from random import randint

chunk_manager = None
element_processor = None
element_storage = None
get_cell = None
CELL_INDEX: int = 5

def update(chunk, x: int, y: int):
    do_skip_over: bool = True
   # pos = (x,y)
   # keep_alive_list = ((x - 1, y), (x, y), (x + 1, y))

    bot = chunk.get_cell(x, y - 1)
    if (bot == 2 or bot in element_storage.gases) and not chunk.is_visited(x,y-1):
        chunk.set_cell(x, y-1, 5)
        chunk.set_cell(x, y, 6 if bot == 2 else bot)
        chunk.keep_alive(and_neighbours=True)
        return
    if bot == 0 or bot in element_storage.burnables:
        if (bot == 0 or randint(0,100)+2 > 100-element_storage.burnables[bot])and not chunk.is_visited(x,y-1) and chunk.set_cell(x, y - 1, 5) :
            chunk.set_cell(x, y, 0)
        do_skip_over = False
       #     pos = (x, y - 1)
            # chunk.keep_alive()
            # chunk.unskip()
    else:
        left = chunk.get_cell(x-1, y) if not chunk.is_visited(x-1,y) else 9
        right = chunk.get_cell(x+1, y) if not chunk.is_visited(x+1,y) else 9
        if left == 2:
            chunk.set_cell(x-1, y, 6)
            do_skip_over = False
        if right == 2:
            chunk.set_cell(x+1, y, 6)
            do_skip_over = False

        if (left in element_storage.gases and right in element_storage.gases ) or (left in element_storage.burnables and right in element_storage.burnables):
            do_skip_over = False
            add = 1 if randint(0, 10) > 4 else -1
            if add == -1:
                if (left in element_storage.gases and randint(0,10) > 6) or (left not in element_storage.gases and randint(0,100)+2 > 100-element_storage.burnables[left]):
                    if chunk.set_cell(x + add, y, 5):
                        chunk.set_cell(x, y, 0)
            else:
                if (right in element_storage.gases and randint(0,10) > 6) or (right not in element_storage.gases and randint(0,100)+2 > 100-element_storage.burnables[right]):
                    if chunk.set_cell(x + add, y, 5):
                        chunk.set_cell(x, y, 0)
                  #  pos = (x + add, y)
            # chunk.keep_alive()
            # chunk.unskip()
        elif left in element_storage.gases or left in element_storage.burnables:
            do_skip_over = False
            add = -1
            if (left in element_storage.gases and randint(0, 10) > 6) or (left not in element_storage.gases and randint(0,100)+2 > 100-element_storage.burnables[left]):
                if chunk.set_cell(x + add, y, 5):
                    chunk.set_cell(x, y, 0)
                   # pos = (x + add, y)
            # chunk.keep_alive()
            # chunk.unskip()
        elif right in element_storage.gases or right in element_storage.burnables:
            do_skip_over = False
            add = 1
            if (right in element_storage.gases and randint(0, 10) > 6) or (right not in element_storage.gases and randint(0,100)+2 > 100-element_storage.burnables[right]):
                if chunk.set_cell(x + add, y, 5):
                    chunk.set_cell(x, y, 0)
              #      pos = (x+add, y)
            # chunk.keep_alive()
            # chunk.unskip()

    if do_skip_over:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
    #else:
    #    chunk.keep_alive()