from random import random, randint, randrange
dummy_chunk = None
chunks = None
def powder_0(chunk, x: int, y: int):
    powder = types[0]
    id = 0
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

def powder_1(chunk, x: int, y: int):
    powder = types[1]
    id = 1
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

def powder_2(chunk, x: int, y: int):
    powder = types[2]
    id = 2
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

def powder_5(chunk, x: int, y: int):
    powder = types[5]
    id = 5
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

def powder_6(chunk, x: int, y: int):
    powder = types[6]
    id = 6
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

def powder_7(chunk, x: int, y: int):
    powder = types[7]
    id = 7
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

def powder_8(chunk, x: int, y: int):
    powder = types[8]
    id = 8
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) :
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

permuts_9 = (
((0, 1, 100), (-1, 1, 30), (1, 1, 30)),
((0, 1, 100), (1, 1, 30), (-1, 1, 30)),
((-1, 1, 30), (0, 1, 100), (1, 1, 30)),
((-1, 1, 30), (1, 1, 30), (0, 1, 100)),
((1, 1, 30), (0, 1, 100), (-1, 1, 30)),
((1, 1, 30), (-1, 1, 30), (0, 1, 100)),)
def powder_9(chunk, x: int, y: int):
    powder = types[9]
    id = 9
    get_cell = chunk.get_cell
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    
        

    


    curr_offsets = permuts_9[randint(0,5)]
    if True:

        pass

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) and get_cell(new_x-1,new_y) == 0 and get_cell(new_x+1, new_y) == 0:
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) and get_cell(new_x-1,new_y) == 0 and get_cell(new_x+1, new_y) == 0:
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited) and get_cell(new_x-1,new_y) == 0 and get_cell(new_x+1, new_y) == 0:
                bottom_cell = chunk.prev[new_y*12+new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[(new_y % 12) * 12 + new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                        
                        if interaction[0] != id:
                            new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                            ly, lx = y, x
                            if new_chunk != chunk:
                                ly, lx = y % 12, x % 12
                            new_chunk.data[ly*12 + lx] = interaction[0]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                        
                        if True:
                            new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                            ly, lx = new_y, new_x
                            if new_chunk != chunk:
                                ly, lx = new_y % 12, new_x % 12
                            new_chunk.data[ly*12 + lx] = interaction[1]
                            if new_chunk != dummy_chunk:
                                new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        iter_counter += 1
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

