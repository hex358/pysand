
############        unrolled.py        ############
# This file is created automatically to maximize  #
# the perfomance via loop unrolling and function  #
# inlining. It's not human-readable.              #
###################################################




from random import random, randint, randrange
from collections import namedtuple
dummy_chunk = None
updated_this_round = set([])
update_types = None
chunks = None

interact_1 = None

interact_2 = None

interact_3 = None

interact_4 = None

interact_5 = None

interact_6 = None

interact_7 = None

interact_8 = None

interact_9 = None

interact_10 = None

interact_11 = None

acc_bits_1 = None


def powder_1(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_2 = None


def powder_2(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, 0)]:
                    interaction = powder.bit_interactions[(-1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, 0)]:
                    interaction = powder.bit_interactions[(1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, 0)]:
                    interaction = powder.bit_interactions[(1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, 0)]:
                    interaction = powder.bit_interactions[(-1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_3 = None


def powder_3(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_4 = None


def powder_4(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_5 = None


def powder_5(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, 0)]:
                    interaction = powder.bit_interactions[(-1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, 0)]:
                    interaction = powder.bit_interactions[(1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, 0)]:
                    interaction = powder.bit_interactions[(1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, 0)]:
                    interaction = powder.bit_interactions[(-1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_6 = None


def powder_6(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, 1)]:
                    interaction = powder.bit_interactions[(0, 1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, 0)]:
                    interaction = powder.bit_interactions[(-1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, 0)]:
                    interaction = powder.bit_interactions[(1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, 1)]:
                    interaction = powder.bit_interactions[(0, 1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, 0)]:
                    interaction = powder.bit_interactions[(1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, 0)]:
                    interaction = powder.bit_interactions[(-1, 0)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_7 = None


def powder_7(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_8 = None


def powder_8(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_9 = None


def powder_9(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if  id_and_bit in acc_bits_9[(0, 1)] and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, 1)]:
                    interaction = powder.bit_interactions[(0, 1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if  id_and_bit in acc_bits_9[(0, 1)] and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, 1)]:
                    interaction = powder.bit_interactions[(0, 1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if id_and_bit in interaction[3]:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        

permuts_10 = (
((0, 1, 100), (-1, 1, 15), (1, 1, 15)),
((0, 1, 100), (1, 1, 15), (-1, 1, 15)),
((-1, 1, 15), (0, 1, 100), (1, 1, 15)),
((-1, 1, 15), (1, 1, 15), (0, 1, 100)),
((1, 1, 15), (0, 1, 100), (-1, 1, 15)),
((1, 1, 15), (-1, 1, 15), (0, 1, 100)),)
replaces = {-1: 0, 0: 0, 1: 0}
acc_bits_10 = None


def powder_10(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
    
    if id_and_bit <= 2560:
        keep = False
        sleep = True
    else:
        cached_left, cached_up, cached_right = (chunk.prev[(y+1)*12+(x-1)] if (0 <= (x-1) < 12 and 0 <= (y+1) < 12) else chunks.get(((chunk.xo*12+(x-1)) // 12, (chunk.yo*12+(y+1)) // 12), dummy_chunk).prev[((y+1) % 12) * 12 + (x-1) % 12]), (chunk.prev[(y+1)*12+(x)] if (0 <= (x) < 12 and 0 <= (y+1) < 12) else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y+1)) // 12), dummy_chunk).prev[((y+1) % 12) * 12 + (x) % 12]), (chunk.prev[(y+1)*12+(x+1)] if (0 <= (x+1) < 12 and 0 <= (y+1) < 12) else chunks.get(((chunk.xo*12+(x+1)) // 12, (chunk.yo*12+(y+1)) // 12), dummy_chunk).prev[((y+1) % 12) * 12 + (x+1) % 12])
        if (cached_left in powder.id_space or cached_right in powder.id_space or cached_up in powder.id_space): 
            keep = False
            sleep = True
        else:
            replaces[-1], replaces[0], replaces[1] = cached_left, cached_up, cached_right
               
        

    


    curr_offsets = permuts_10[randint(0,5)]
    if True:

        pass

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = replaces[add_x]#(new_x,new_y)
                if bottom_cell in powder.bit_interactions[(add_x, add_y)]:
                    interaction = powder.bit_interactions[(add_x, add_y)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if False:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if interaction[0] > 255 else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if interaction[1] > 255 else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = replaces[add_x]#(new_x,new_y)
                if bottom_cell in powder.bit_interactions[(add_x, add_y)]:
                    interaction = powder.bit_interactions[(add_x, add_y)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if False:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if interaction[0] > 255 else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if interaction[1] > 255 else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = replaces[add_x]#(new_x,new_y)
                if bottom_cell in powder.bit_interactions[(add_x, add_y)]:
                    interaction = powder.bit_interactions[(add_x, add_y)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if False:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if interaction[0] > 255 else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if interaction[1] > 255 else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        iter_counter += 1
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        


acc_bits_11 = None


def powder_11(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if  id_and_bit in acc_bits_11[(0, 1)] and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, 1)]:
                    interaction = powder.bit_interactions[(0, 1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, -1)]:
                    interaction = powder.bit_interactions[(0, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if  id_and_bit in acc_bits_11[(0, 1)] and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(0, 1)]:
                    interaction = powder.bit_interactions[(0, 1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(1, -1)]:
                    interaction = powder.bit_interactions[(1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                if bottom_cell in powder.bit_interactions[(-1, -1)]:
                    interaction = powder.bit_interactions[(-1, -1)][bottom_cell]
                    if True:#id_and_bit in interaction[3]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            if interaction[0] != id_and_bit:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            chunk.is_uniform = False
            chunk.first_assign = False
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        

