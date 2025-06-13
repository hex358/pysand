from random import random
dummy_chunk = None
chunks = None
def powder_1(chunk, x: int, y: int):
    powder = types[1]
    sleep: bool = True
    keep = True
    
        
    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
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
    sleep: bool = True
    keep = True
    
        
    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
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
    sleep: bool = True
    keep = True
    
        
    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
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
    sleep: bool = True
    keep = True
    
        
    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
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
    sleep: bool = True
    keep = True
    
        
    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
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
    sleep: bool = True
    keep = True
    
        
    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if not ((new_x,new_y) in chunk.visited if 0 <= new_x < 12 and 0 <= new_y < 12 else (new_x % 12, new_y % 12) in chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).visited):
                bottom_cell = chunk.prev[new_y,new_x] if (0 <= new_x < 12 and 0 <= new_y < 12) else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk).prev[new_y % 12, new_x % 12]
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
                    if 100*random() > 100-50 and  (interaction[2] == 100 or random()*100 > 100-interaction[2]):
                        
                        new_chunk = chunk if 0 <= x < 12 and 0 <= y < 12 else chunks.get(((chunk.xo*12+x) // 12, (chunk.yo*12+y) // 12), dummy_chunk)
                        ly, lx = y, x
                        if new_chunk != chunk:
                            ly, lx = y % 12, x % 12
                        new_chunk.data[ly, lx] = interaction[0]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                        
                        new_chunk = chunk if 0 <= new_x < 12 and 0 <= new_y < 12 else chunks.get(((chunk.xo*12+new_x) // 12, (chunk.yo*12+new_y) // 12), dummy_chunk)
                        ly, lx = new_y, new_x
                        if new_chunk != chunk:
                            ly, lx = new_y % 12, new_x % 12
                        new_chunk.data[ly, lx] = interaction[1]
                        if new_chunk != dummy_chunk:
                            new_chunk.visited.add((lx, ly))
                            
                    sleep = False
                    keep = False
        
            
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
        

