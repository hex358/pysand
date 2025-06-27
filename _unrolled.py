
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
dirs = {(-1,0): 0, (0,-1):0, (1,0):0, (0,1): 0}

interact_99 = None

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
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
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
                interaction = powder.bit_interactions[(0, 1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 0, y + -1
            if  id_and_bit in acc_bits_6[(0, -1)] and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-0.06 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, 1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 0, y + -1
            if  id_and_bit in acc_bits_6[(0, -1)] and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-0.06 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, 0)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if   id_and_bit == 2305 and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, 1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if   id_and_bit == 2305 and  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(0, 1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
                        
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                interaction = powder.bit_interactions[(-1, -1)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if True:
                                
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
    
    if (id_and_bit > 2560 and chunk.get_cell(x-1,y-1) != 10 and chunk.get_cell(x+1,y-1) != 10 and chunk.get_cell(x, y-1) != 10) or\
        (id_and_bit == 2560 and chunk.get_cell(x-1,y-1) == 0 and chunk.get_cell(x+1,y-1) == 0 and chunk.get_cell(x, y-1) == 0):
        chunk.set_cell(x,y,1)
        keep = False
        sleep = True
        return
    
    if id_and_bit >= 2570:
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
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if False:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if False:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True :
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if False:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
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
            
        

permuts_11 = (
((0, -1, 100), (0, 1, 100), (1, 0, 100), (-1, 0, 100), (0, 0, 100)),
((0, -1, 100), (0, 1, 100), (1, 0, 100), (0, 0, 100), (-1, 0, 100)),
((0, -1, 100), (0, 1, 100), (-1, 0, 100), (1, 0, 100), (0, 0, 100)),
((0, -1, 100), (0, 1, 100), (-1, 0, 100), (0, 0, 100), (1, 0, 100)),
((0, -1, 100), (0, 1, 100), (0, 0, 100), (1, 0, 100), (-1, 0, 100)),
((0, -1, 100), (0, 1, 100), (0, 0, 100), (-1, 0, 100), (1, 0, 100)),
((0, -1, 100), (1, 0, 100), (0, 1, 100), (-1, 0, 100), (0, 0, 100)),
((0, -1, 100), (1, 0, 100), (0, 1, 100), (0, 0, 100), (-1, 0, 100)),
((0, -1, 100), (1, 0, 100), (-1, 0, 100), (0, 1, 100), (0, 0, 100)),
((0, -1, 100), (1, 0, 100), (-1, 0, 100), (0, 0, 100), (0, 1, 100)),
((0, -1, 100), (1, 0, 100), (0, 0, 100), (0, 1, 100), (-1, 0, 100)),
((0, -1, 100), (1, 0, 100), (0, 0, 100), (-1, 0, 100), (0, 1, 100)),
((0, -1, 100), (-1, 0, 100), (0, 1, 100), (1, 0, 100), (0, 0, 100)),
((0, -1, 100), (-1, 0, 100), (0, 1, 100), (0, 0, 100), (1, 0, 100)),
((0, -1, 100), (-1, 0, 100), (1, 0, 100), (0, 1, 100), (0, 0, 100)),
((0, -1, 100), (-1, 0, 100), (1, 0, 100), (0, 0, 100), (0, 1, 100)),
((0, -1, 100), (-1, 0, 100), (0, 0, 100), (0, 1, 100), (1, 0, 100)),
((0, -1, 100), (-1, 0, 100), (0, 0, 100), (1, 0, 100), (0, 1, 100)),
((0, -1, 100), (0, 0, 100), (0, 1, 100), (1, 0, 100), (-1, 0, 100)),
((0, -1, 100), (0, 0, 100), (0, 1, 100), (-1, 0, 100), (1, 0, 100)),
((0, -1, 100), (0, 0, 100), (1, 0, 100), (0, 1, 100), (-1, 0, 100)),
((0, -1, 100), (0, 0, 100), (1, 0, 100), (-1, 0, 100), (0, 1, 100)),
((0, -1, 100), (0, 0, 100), (-1, 0, 100), (0, 1, 100), (1, 0, 100)),
((0, -1, 100), (0, 0, 100), (-1, 0, 100), (1, 0, 100), (0, 1, 100)),
((0, 1, 100), (0, -1, 100), (1, 0, 100), (-1, 0, 100), (0, 0, 100)),
((0, 1, 100), (0, -1, 100), (1, 0, 100), (0, 0, 100), (-1, 0, 100)),
((0, 1, 100), (0, -1, 100), (-1, 0, 100), (1, 0, 100), (0, 0, 100)),
((0, 1, 100), (0, -1, 100), (-1, 0, 100), (0, 0, 100), (1, 0, 100)),
((0, 1, 100), (0, -1, 100), (0, 0, 100), (1, 0, 100), (-1, 0, 100)),
((0, 1, 100), (0, -1, 100), (0, 0, 100), (-1, 0, 100), (1, 0, 100)),
((0, 1, 100), (1, 0, 100), (0, -1, 100), (-1, 0, 100), (0, 0, 100)),
((0, 1, 100), (1, 0, 100), (0, -1, 100), (0, 0, 100), (-1, 0, 100)),
((0, 1, 100), (1, 0, 100), (-1, 0, 100), (0, -1, 100), (0, 0, 100)),
((0, 1, 100), (1, 0, 100), (-1, 0, 100), (0, 0, 100), (0, -1, 100)),
((0, 1, 100), (1, 0, 100), (0, 0, 100), (0, -1, 100), (-1, 0, 100)),
((0, 1, 100), (1, 0, 100), (0, 0, 100), (-1, 0, 100), (0, -1, 100)),
((0, 1, 100), (-1, 0, 100), (0, -1, 100), (1, 0, 100), (0, 0, 100)),
((0, 1, 100), (-1, 0, 100), (0, -1, 100), (0, 0, 100), (1, 0, 100)),
((0, 1, 100), (-1, 0, 100), (1, 0, 100), (0, -1, 100), (0, 0, 100)),
((0, 1, 100), (-1, 0, 100), (1, 0, 100), (0, 0, 100), (0, -1, 100)),
((0, 1, 100), (-1, 0, 100), (0, 0, 100), (0, -1, 100), (1, 0, 100)),
((0, 1, 100), (-1, 0, 100), (0, 0, 100), (1, 0, 100), (0, -1, 100)),
((0, 1, 100), (0, 0, 100), (0, -1, 100), (1, 0, 100), (-1, 0, 100)),
((0, 1, 100), (0, 0, 100), (0, -1, 100), (-1, 0, 100), (1, 0, 100)),
((0, 1, 100), (0, 0, 100), (1, 0, 100), (0, -1, 100), (-1, 0, 100)),
((0, 1, 100), (0, 0, 100), (1, 0, 100), (-1, 0, 100), (0, -1, 100)),
((0, 1, 100), (0, 0, 100), (-1, 0, 100), (0, -1, 100), (1, 0, 100)),
((0, 1, 100), (0, 0, 100), (-1, 0, 100), (1, 0, 100), (0, -1, 100)),
((1, 0, 100), (0, -1, 100), (0, 1, 100), (-1, 0, 100), (0, 0, 100)),
((1, 0, 100), (0, -1, 100), (0, 1, 100), (0, 0, 100), (-1, 0, 100)),
((1, 0, 100), (0, -1, 100), (-1, 0, 100), (0, 1, 100), (0, 0, 100)),
((1, 0, 100), (0, -1, 100), (-1, 0, 100), (0, 0, 100), (0, 1, 100)),
((1, 0, 100), (0, -1, 100), (0, 0, 100), (0, 1, 100), (-1, 0, 100)),
((1, 0, 100), (0, -1, 100), (0, 0, 100), (-1, 0, 100), (0, 1, 100)),
((1, 0, 100), (0, 1, 100), (0, -1, 100), (-1, 0, 100), (0, 0, 100)),
((1, 0, 100), (0, 1, 100), (0, -1, 100), (0, 0, 100), (-1, 0, 100)),
((1, 0, 100), (0, 1, 100), (-1, 0, 100), (0, -1, 100), (0, 0, 100)),
((1, 0, 100), (0, 1, 100), (-1, 0, 100), (0, 0, 100), (0, -1, 100)),
((1, 0, 100), (0, 1, 100), (0, 0, 100), (0, -1, 100), (-1, 0, 100)),
((1, 0, 100), (0, 1, 100), (0, 0, 100), (-1, 0, 100), (0, -1, 100)),
((1, 0, 100), (-1, 0, 100), (0, -1, 100), (0, 1, 100), (0, 0, 100)),
((1, 0, 100), (-1, 0, 100), (0, -1, 100), (0, 0, 100), (0, 1, 100)),
((1, 0, 100), (-1, 0, 100), (0, 1, 100), (0, -1, 100), (0, 0, 100)),
((1, 0, 100), (-1, 0, 100), (0, 1, 100), (0, 0, 100), (0, -1, 100)),
((1, 0, 100), (-1, 0, 100), (0, 0, 100), (0, -1, 100), (0, 1, 100)),
((1, 0, 100), (-1, 0, 100), (0, 0, 100), (0, 1, 100), (0, -1, 100)),
((1, 0, 100), (0, 0, 100), (0, -1, 100), (0, 1, 100), (-1, 0, 100)),
((1, 0, 100), (0, 0, 100), (0, -1, 100), (-1, 0, 100), (0, 1, 100)),
((1, 0, 100), (0, 0, 100), (0, 1, 100), (0, -1, 100), (-1, 0, 100)),
((1, 0, 100), (0, 0, 100), (0, 1, 100), (-1, 0, 100), (0, -1, 100)),
((1, 0, 100), (0, 0, 100), (-1, 0, 100), (0, -1, 100), (0, 1, 100)),
((1, 0, 100), (0, 0, 100), (-1, 0, 100), (0, 1, 100), (0, -1, 100)),
((-1, 0, 100), (0, -1, 100), (0, 1, 100), (1, 0, 100), (0, 0, 100)),
((-1, 0, 100), (0, -1, 100), (0, 1, 100), (0, 0, 100), (1, 0, 100)),
((-1, 0, 100), (0, -1, 100), (1, 0, 100), (0, 1, 100), (0, 0, 100)),
((-1, 0, 100), (0, -1, 100), (1, 0, 100), (0, 0, 100), (0, 1, 100)),
((-1, 0, 100), (0, -1, 100), (0, 0, 100), (0, 1, 100), (1, 0, 100)),
((-1, 0, 100), (0, -1, 100), (0, 0, 100), (1, 0, 100), (0, 1, 100)),
((-1, 0, 100), (0, 1, 100), (0, -1, 100), (1, 0, 100), (0, 0, 100)),
((-1, 0, 100), (0, 1, 100), (0, -1, 100), (0, 0, 100), (1, 0, 100)),
((-1, 0, 100), (0, 1, 100), (1, 0, 100), (0, -1, 100), (0, 0, 100)),
((-1, 0, 100), (0, 1, 100), (1, 0, 100), (0, 0, 100), (0, -1, 100)),
((-1, 0, 100), (0, 1, 100), (0, 0, 100), (0, -1, 100), (1, 0, 100)),
((-1, 0, 100), (0, 1, 100), (0, 0, 100), (1, 0, 100), (0, -1, 100)),
((-1, 0, 100), (1, 0, 100), (0, -1, 100), (0, 1, 100), (0, 0, 100)),
((-1, 0, 100), (1, 0, 100), (0, -1, 100), (0, 0, 100), (0, 1, 100)),
((-1, 0, 100), (1, 0, 100), (0, 1, 100), (0, -1, 100), (0, 0, 100)),
((-1, 0, 100), (1, 0, 100), (0, 1, 100), (0, 0, 100), (0, -1, 100)),
((-1, 0, 100), (1, 0, 100), (0, 0, 100), (0, -1, 100), (0, 1, 100)),
((-1, 0, 100), (1, 0, 100), (0, 0, 100), (0, 1, 100), (0, -1, 100)),
((-1, 0, 100), (0, 0, 100), (0, -1, 100), (0, 1, 100), (1, 0, 100)),
((-1, 0, 100), (0, 0, 100), (0, -1, 100), (1, 0, 100), (0, 1, 100)),
((-1, 0, 100), (0, 0, 100), (0, 1, 100), (0, -1, 100), (1, 0, 100)),
((-1, 0, 100), (0, 0, 100), (0, 1, 100), (1, 0, 100), (0, -1, 100)),
((-1, 0, 100), (0, 0, 100), (1, 0, 100), (0, -1, 100), (0, 1, 100)),
((-1, 0, 100), (0, 0, 100), (1, 0, 100), (0, 1, 100), (0, -1, 100)),
((0, 0, 100), (0, -1, 100), (0, 1, 100), (1, 0, 100), (-1, 0, 100)),
((0, 0, 100), (0, -1, 100), (0, 1, 100), (-1, 0, 100), (1, 0, 100)),
((0, 0, 100), (0, -1, 100), (1, 0, 100), (0, 1, 100), (-1, 0, 100)),
((0, 0, 100), (0, -1, 100), (1, 0, 100), (-1, 0, 100), (0, 1, 100)),
((0, 0, 100), (0, -1, 100), (-1, 0, 100), (0, 1, 100), (1, 0, 100)),
((0, 0, 100), (0, -1, 100), (-1, 0, 100), (1, 0, 100), (0, 1, 100)),
((0, 0, 100), (0, 1, 100), (0, -1, 100), (1, 0, 100), (-1, 0, 100)),
((0, 0, 100), (0, 1, 100), (0, -1, 100), (-1, 0, 100), (1, 0, 100)),
((0, 0, 100), (0, 1, 100), (1, 0, 100), (0, -1, 100), (-1, 0, 100)),
((0, 0, 100), (0, 1, 100), (1, 0, 100), (-1, 0, 100), (0, -1, 100)),
((0, 0, 100), (0, 1, 100), (-1, 0, 100), (0, -1, 100), (1, 0, 100)),
((0, 0, 100), (0, 1, 100), (-1, 0, 100), (1, 0, 100), (0, -1, 100)),
((0, 0, 100), (1, 0, 100), (0, -1, 100), (0, 1, 100), (-1, 0, 100)),
((0, 0, 100), (1, 0, 100), (0, -1, 100), (-1, 0, 100), (0, 1, 100)),
((0, 0, 100), (1, 0, 100), (0, 1, 100), (0, -1, 100), (-1, 0, 100)),
((0, 0, 100), (1, 0, 100), (0, 1, 100), (-1, 0, 100), (0, -1, 100)),
((0, 0, 100), (1, 0, 100), (-1, 0, 100), (0, -1, 100), (0, 1, 100)),
((0, 0, 100), (1, 0, 100), (-1, 0, 100), (0, 1, 100), (0, -1, 100)),
((0, 0, 100), (-1, 0, 100), (0, -1, 100), (0, 1, 100), (1, 0, 100)),
((0, 0, 100), (-1, 0, 100), (0, -1, 100), (1, 0, 100), (0, 1, 100)),
((0, 0, 100), (-1, 0, 100), (0, 1, 100), (0, -1, 100), (1, 0, 100)),
((0, 0, 100), (-1, 0, 100), (0, 1, 100), (1, 0, 100), (0, -1, 100)),
((0, 0, 100), (-1, 0, 100), (1, 0, 100), (0, -1, 100), (0, 1, 100)),
((0, 0, 100), (-1, 0, 100), (1, 0, 100), (0, 1, 100), (0, -1, 100)),)
replaces = {-1: 0, 0: 0, 1: 0}
acc_bits_11 = None


def powder_11(chunk, id_and_bit, curr_bit, x: int, y: int):


    powder = update_types[id_and_bit]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    res_x, res_y = None, None
    
    
        
    left = chunk.prev[(y)*12+(x-1)] if (0 <= (x-1) < 12 and 0 <= (y) < 12) else chunks.get(((chunk.xo*12+(x-1)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk).prev[((y) % 12) * 12 + (x-1) % 12]
    right = chunk.prev[(y)*12+(x+1)] if (0 <= (x+1) < 12 and 0 <= (y) < 12) else chunks.get(((chunk.xo*12+(x+1)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk).prev[((y) % 12) * 12 + (x+1) % 12]
    bottom = chunk.prev[(y-1)*12+(x)] if (0 <= (x) < 12 and 0 <= (y-1) < 12) else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y-1)) // 12), dummy_chunk).prev[((y-1) % 12) * 12 + (x) % 12]
    top = chunk.prev[(y+1)*12+(x)] if (0 <= (x) < 12 and 0 <= (y+1) < 12) else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y+1)) // 12), dummy_chunk).prev[((y+1) % 12) * 12 + (x) % 12]
    
    dirs[(-1,0)], dirs[(1,0)], dirs[(0,-1)], dirs[(0,1)] = left, right, bottom, top
    exclude = (-2,-2)
    
    if not chunk.even_tick:
        if left in powder.priority_types:
            exclude = (-1,0)
        elif right in powder.priority_types:
            exclude = (1,0)
    else:
        if bottom in powder.priority_types:
            exclude = (0,-1)
        elif top in powder.priority_types:
            exclude = (0,1)
    
    
    
    if exclude != (-2,-2):
        add_x, add_y, prob = exclude[0], exclude[1], 100
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = dirs[(add_x,add_y)] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            
        keep = False
        iter_counter -= 1

    


    curr_offsets = permuts_11[randint(0,119)]
    if True:

        pass

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = dirs[(add_x,add_y)] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = dirs[(add_x,add_y)] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = dirs[(add_x,add_y)] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = dirs[(add_x,add_y)] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if  (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = dirs[(add_x,add_y)] if (add_x,add_y) != (0,0) else id_and_bit
                interaction = powder.bit_interactions[(add_x, add_y)].get(bottom_cell, None)
                if interaction is not None:
                    if True and chunk.tick_modulus[interaction[8]]:
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            keep = False
                            if not interaction[6]:
                                
                                new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                ly, lx = (y), (x)
                                if new_chunk != chunk:
                                    ly, lx = (y) % 12, (x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[0] if not interaction[4] else id_and_bit + interaction[0])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                            if interaction[1] != bottom_cell:
                                
                                new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                ly, lx = (new_y), (new_x)
                                if new_chunk != chunk:
                                    ly, lx = (new_y) % 12, (new_x) % 12
                                new_chunk.data[ly*12 + lx] = (interaction[1] if not interaction[5] else id_and_bit + interaction[1])
                                new_chunk.visited.add((lx, ly))
                                new_chunk.is_uniform = False
                                new_chunk.first_assign = False
                                
                        res_x, res_y = new_x, new_y
                        sleep = False
                        
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
            
        

