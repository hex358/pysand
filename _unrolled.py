
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

interact_5 = None

interact_6 = None

interact_7 = None

interact_8 = None

interact_9 = None

interact_10 = None


def powder_1(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = -1
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_1[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_1[(-1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_1[(1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_1[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_1[(1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_1[(-1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        



def powder_2(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = -1
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_2[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_2[(-1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_2[(1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_2[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_2[(1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_2[(-1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        



def powder_5(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = -1
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_5[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_5[(-1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_5[(1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_5[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_5[(1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_5[(-1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        



def powder_6(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = -1
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_6[(0, 1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_6[(-1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_6[(1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + 1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_6[(0, 1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_6[(1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + 0
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_6[(-1, 0, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        



def powder_7(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = -1
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_7[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_7[(-1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_7[(1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_7[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_7[(1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_7[(-1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        



def powder_8(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = -1
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_8[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_8[(-1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_8[(1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_8[(0, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_8[(1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_8[(-1, -1, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-30 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        



def powder_9(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = (chunk.prev[(y)*12+(x)] & 0xFF if (0 <= (x) < 12 and 0 <= (y) < 12) else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk).prev[((y) % 12) * 12 + (x) % 12] & 0xFF)
    res_x, res_y = None, None
    
    
        

    

    if chunk.ticks % 2 == 0:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(0, -1, False)], interact_9[(0, -1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(-1, -1, False)], interact_9[(-1, -1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(1, -1, False)], interact_9[(1, -1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(0, 1, False)], interact_9[(0, 1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            

    else:

        pass
        if keep:
            new_x, new_y = x + 0, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(0, -1, False)], interact_9[(0, -1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 0, y + 1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(0, 1, False)], interact_9[(0, 1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + 1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(1, -1, False)], interact_9[(1, -1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
        if keep:
            new_x, new_y = x + -1, y + -1
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = chunk.prev[(new_y)*12+(new_x)] if (0 <= (new_x) < 12 and 0 <= (new_y) < 12) else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk).prev[((new_y) % 12) * 12 + (new_x) % 12]
                dict1, dict2 = interact_9[(-1, -1, False)], interact_9[(-1, -1, True)] #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if True else 0
                if bit_1 in dict1 or (True and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if True and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-50 and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if True:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
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

def powder_10(chunk, id, x: int, y: int):
    powder = update_types[id]
    get_cell = chunk.get_cell
    
    set_cell = chunk.set_cell
    sleep: bool = True
    keep = True
    iter_counter: int = 0
    curr_bit: int = (chunk.prev[(y)*12+(x)] & 0xFF if (0 <= (x) < 12 and 0 <= (y) < 12) else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk).prev[((y) % 12) * 12 + (x) % 12] & 0xFF)
    res_x, res_y = None, None
    
    
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
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = replaces[add_x]#(new_x,new_y)
                dict1, dict2 = interact_10[(add_x, add_y, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if curr_bit > 0:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                            
                            if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12:
                                chunk.data[( new_y)*12+(new_x)] = (chunk.data[( new_y)*12+(new_x)] & 0xFF00) | (( curr_bit - 1) & 0xFF)
                            else:
                                gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + ( new_y)
                                target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                local_x, local_y = gx % 12, gy % 12
                                target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | (( curr_bit - 1) & 0xFF)
                            
                            if curr_bit <= 0:
                                sleep = True 
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = replaces[add_x]#(new_x,new_y)
                dict1, dict2 = interact_10[(add_x, add_y, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if curr_bit > 0:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                            
                            if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12:
                                chunk.data[( new_y)*12+(new_x)] = (chunk.data[( new_y)*12+(new_x)] & 0xFF00) | (( curr_bit - 1) & 0xFF)
                            else:
                                gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + ( new_y)
                                target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                local_x, local_y = gx % 12, gy % 12
                                target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | (( curr_bit - 1) & 0xFF)
                            
                            if curr_bit <= 0:
                                sleep = True 
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        iter_counter += 1
        
            

        add_x, add_y, prob =  curr_offsets[iter_counter]
        if keep:
            new_x, new_y = x + add_x, y + add_y
            if (not (((new_x),( new_y)) in chunk.visited if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12 else ((new_x) % 12, ( new_y) % 12) in chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+( new_y)) // 12), dummy_chunk).visited) ) and True:
                bottom_cell = replaces[add_x]#(new_x,new_y)
                dict1, dict2 = interact_10[(add_x, add_y, False)], None #
                bit_1 = bottom_cell >> 8
                bit_2 = bottom_cell & 0xFF if False else 0
                if bit_1 in dict1 or (False and bit_2 in dict2):
                    interaction = None
                    is_bit_2 = False
                    if False and bit_2 in dict2:
                        is_bit_2 = True
                        interaction = dict2[bit_2]
                    else:
                        interaction = dict1[bit_1]
                    if (not is_bit_2 or interaction[3] != curr_bit) and (curr_bit == -1 or curr_bit in interaction[6]):
                        if 100*random() > 100-prob and  (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                            
                            
                            
                            if interaction[5]:
                                if interaction[0] != id:
                                    
                                    new_chunk = chunk if 0 <= (x) < 12 and 0 <= (y) < 12 else chunks.get(((chunk.xo*12+(x)) // 12, (chunk.yo*12+(y)) // 12), dummy_chunk)
                                    ly, lx = (y), (x)
                                    if new_chunk != chunk:
                                        ly, lx = (y) % 12, (x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[0] << 8 | interaction[3])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                                if curr_bit > 0:
                                    
                                    new_chunk = chunk if 0 <= (new_x) < 12 and 0 <= (new_y) < 12 else chunks.get(((chunk.xo*12+(new_x)) // 12, (chunk.yo*12+(new_y)) // 12), dummy_chunk)
                                    ly, lx = (new_y), (new_x)
                                    if new_chunk != chunk:
                                        ly, lx = (new_y) % 12, (new_x) % 12
                                    new_chunk.data[ly*12 + lx] = (interaction[1] << 8 | interaction[4])# << 8
                                    new_chunk.visited.add((lx, ly))
                                    
                            else:
                                
                                if 0 <= (x) < 12 and 0 <= (y) < 12:
                                    chunk.data[(y)*12+(x)] = (chunk.data[(y)*12+(x)] & 0xFF00) | ((interaction[3]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (x), chunk.yo * 12 + (y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[3]) & 0xFF)
                                
                                
                                if 0 <= (new_x) < 12 and 0 <= (new_y) < 12:
                                    chunk.data[(new_y)*12+(new_x)] = (chunk.data[(new_y)*12+(new_x)] & 0xFF00) | ((interaction[4]) & 0xFF)
                                else:
                                    gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + (new_y)
                                    target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                    local_x, local_y = gx % 12, gy % 12
                                    target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | ((interaction[4]) & 0xFF)
                                
                            
                            
                            if 0 <= (new_x) < 12 and 0 <= ( new_y) < 12:
                                chunk.data[( new_y)*12+(new_x)] = (chunk.data[( new_y)*12+(new_x)] & 0xFF00) | (( curr_bit - 1) & 0xFF)
                            else:
                                gx, gy = chunk.xo * 12 + (new_x), chunk.yo * 12 + ( new_y)
                                target = chunks.get((gx // 12, gy // 12), dummy_chunk)
                                local_x, local_y = gx % 12, gy % 12
                                target.data[local_y*12+local_x] = (target.data[local_y*12+local_x] & 0xFF00) | (( curr_bit - 1) & 0xFF)
                            
                            if curr_bit <= 0:
                                sleep = True 
                            
                        res_x, res_y = new_x, new_y
                        sleep = False
                        keep = False
        iter_counter += 1
        
            
    if sleep:
        
        chunk.skipped_over_count += 1
        
    else:
        
        xo,yo = chunk.xo, chunk.yo
        chunk.update_intensity = MAX_UPDATE_INTENSITY
        if not chunk in updated_this_round:
            updated_this_round.add(chunk)
            chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
        
        if res_x is not None:
            
            xo,yo = chunk.xo, chunk.yo
            chunk.update_intensity = MAX_UPDATE_INTENSITY
            if not chunk in updated_this_round:
                updated_this_round.add(chunk)
                chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
                chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
            
        

