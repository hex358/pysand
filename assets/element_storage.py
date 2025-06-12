TAGS = ["--no-processing"]
USE_MODULES = ["chunk_manager", "mainloop"]
modules_dict = {}
chunk_manager = None
mainloop = None
ELEMENT_LIST = ["sand", "water", "lava", "steam", "dirt"]

import importlib
import sys
import numpy as np
from random import randint

elements_dict = {}
element_calls = {}
elements = []

burnables: dict[int] = {4: 10}
solids: set[int] = {9,3,4,8}
soft: set[int] = {0,2,6}
skip: set[int] = {0,9,3,4,8}
gases: set[int] = {6, 0}

interactions = {
    2: {7:[8,False]}, # element: {interacts with: turns into; True if turn itself}
    7: {2:[8,True]}
}

interactables = {2,7}

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Powder:
    index: int = 1
    fall_offsets: list = field(default_factory=list)
    #: dict = field(default_factory=dict) # element: [h mix probability, v mix probability]
    interact_with_types: dict = field(default_factory=dict) # element: itself turns into.., type turns into.., interaction probability

def create_unrolled():
    header = """
    powder = types[chunk.prev[y,x]]
    get_cell = chunk.get_cell
    set_cell = chunk.get_cell
    sleep: bool = True
    even_tick = chunk.ticks % 2 == 0
    length = len(powder.fall_offsets)
    keep = True
    """
    middle = """
        move_probability = offset[2]
        new_x, new_y = x + offset[0], y + offset[1]
        if chunk.is_visited(new_x, new_y): continue
        bottom_cell = get_cell(new_x,new_y)
        bottom_mix = powder.mix_with_types.get(bottom_cell, default_prob)[0 if offset[1] == 0 else 1]
        if bottom_mix > 0:
            if (move_probability == 100 or randint(0,100) > 100-move_probability) and (bottom_mix == 100 or randint(0,100) > 100-bottom_mix):
                chunk.set_cell(x, y, bottom_cell)
                chunk.set_cell(new_x, new_y, powder.index)
            sleep = False
            keep = False
        elif bottom_cell in powder.interact_with_types:
            interaction = powder.interact_with_types[bottom_cell]
            if interaction[2] > 0:
                if (move_probability == 100 or randint(0,100) > 100-move_probability) and (interaction[2] == 100 or randint(0,100) > 100-interaction[2]):
                    chunk.set_cell(x, y, interaction[0])
                    chunk.set_cell(new_x, new_y, interaction[1])
                sleep = False
            keep = False
    """



types = {
    1: Powder(index=1,
            fall_offsets=[(0,-1,100),(-1,-1,50),(1,-1,50)],
            #mix_with_types={0: (100,100), 2: (20,20)},
            interact_with_types={0: (0, 1, 100)}),
    2: Powder(index=2,
              fall_offsets=[(0, -1, 100), (-1, 0, 50), (1, 0, 50)],
              #mix_with_types={0: (100,100)},
              interact_with_types={0: (0, 2, 100)})

}

default_prob = (0, 0)
def update_powder(chunk, x: int, y: int):
    powder = types[chunk.prev[y,x]]
    get_cell = chunk.get_cell
    set_cell = chunk.get_cell
    sleep: bool = True
    even_tick = chunk.ticks % 2 == 0
    length = len(powder.fall_offsets)

    for i in range(length):
        offset = powder.fall_offsets[i if even_tick or i == 0 else -i]
        move_probability = offset[2]
        new_x, new_y = x + offset[0], y + offset[1]
        if chunk.is_visited(new_x, new_y): continue
        bottom_cell = get_cell(new_x,new_y)
        #bottom_mix = 0 if bottom_cell in mix_with_types#powder.mix_with_types.get(bottom_cell, default_prob)[0 if offset[1] == 0 else 1]
        # if bottom_mix > 0:
        #     if (move_probability == 100 or randint(0,100) > 100-move_probability) and (bottom_mix == 100 or randint(0,100) > 100-bottom_mix):
        #         chunk.set_cell(x, y, bottom_cell)
        #         chunk.set_cell(new_x, new_y, powder.index)
        #     sleep = False
        #     break
        if bottom_cell in powder.interact_with_types:
            interaction = powder.interact_with_types[bottom_cell]
            if interaction[2] > 0:
                if (move_probability == 100 or randint(0,100) > 100-move_probability) and (interaction[2] == 100 or randint(0,100) > 100-interaction[2]):
                    chunk.set_cell(x, y, interaction[0])
                    chunk.set_cell(new_x, new_y, interaction[1])
                sleep = False
            break

    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)


clears = {}
def _ready() -> None:
    for element_name in ELEMENT_LIST:
        element = importlib.import_module(f"elements.{element_name}")
        elements_dict[element_name] = element; elements.append(element)
        element.chunk_manager = chunk_manager
        element.get_cell = chunk_manager.get_cell
        element_calls[element.CELL_INDEX] = element.update
        element.element_storage = sys.modules[__name__]
        if hasattr(element, "clear"):
            clears[element] = element.clear