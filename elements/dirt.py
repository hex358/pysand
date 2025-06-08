from random import randint

chunk_manager = None
element_storage = None
element_processor = None
get_cell = None
CELL_INDEX: int = 7

def update(chunk, x: int, y: int):
    bottom = chunk.get_cell(x,y-1)
    do_skip_over = True
    #pos = (x, y)
    #keep_alive_list = ((x-1,y),(x,y),(x+1,y))

    if bottom == 0:
        do_skip_over = False
        if chunk.set_cell(x,y - 1,7):
            chunk.set_cell(x, y, bottom)
            #pos = (x,y-1)
            # keep_alive_list.append((x-1,y))
            # keep_alive_list.append((x + 1, y))
            # keep_alive_list.append((x, y))
        # chunk.unskip()
        # chunk.keep_alive()
    else:
        left = chunk.get_cell(x - 1,y - 1)
        if left in element_storage.soft and chunk.get_cell(x - 1,y) in element_storage.soft:
            do_skip_over = False
            if randint(0,11) > 9:
                if chunk.set_cell(x - 1, y - 1, 7):
                    chunk.set_cell(x,y,left)
                    #pos = (x - 1, y - 1)
            # chunk.unskip()
            # chunk.keep_alive()

        else:
            right = chunk.get_cell(x + 1,y - 1)
            if right in element_storage.soft and chunk.get_cell(x + 1,y) in element_storage.soft:
                do_skip_over = False
                if randint(0, 11) > 9:
                    if chunk.set_cell(x + 1, y - 1, 7):
                        chunk.set_cell(x, y, right)
                       # pos = (x + 1, y - 1)
                # chunk.unskip()
                # chunk.keep_alive()

    if do_skip_over:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        # #chunk_manager.get_chunk()
        # new_chunk = chunk.get_chunk(pos[0],pos[1])
        # new_chunk.unskip()
        # new_chunk.keep_alive()
        # if (y+1) // 16 != 0:
        #     for coord in keep_alive_list:
        #         new_chunk = chunk.get_chunk(coord[0], coord[1]+1)
        #         new_chunk.unskip()
        #         new_chunk.keep_alive()