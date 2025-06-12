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

import importlib
imported = None
def create_unrolled():
    result = ""

    file_header = """from random import random
dummy_chunk = None
chunks = None
"""

    func_header = """
    powder = types[{id}]
    #get_cell = chunk.get_cell
    #set_cell = chunk.get_cell
    sleep: bool = True
    keep = True

    """

    func_middle = """
        if keep:
            move_probability = {prob}
            new_x, new_y = x + {x}, y + {y}
            if not {is_visited_inline}:
                bottom_cell = {get_cell_inline}
                if bottom_cell in powder.interact_with_types:
                    interaction = powder.interact_with_types[bottom_cell]
                    if (move_probability == 100 or random()*100 > 100-move_probability) and (interaction[{interaction_index}] == 100 or random()*100 > 100-interaction[{interaction_index}]):
                        {set_cell_inline}#chunk.set_cell(x, y, interaction[0])
                        {set_cell_inline_new}#chunk.set_cell(new_x, new_y, interaction[1])
                    sleep = False
                    keep = False

    """

    func_bottom = """
    if sleep:
        chunk.skip_over()
    else:
        chunk.keep_alive(and_neighbours=True)
    """

    get_cell_lambda = "chunk.prev[new_y,new_x] if (0 <= new_x < CHUNK_SIZE and 0 <= new_y < CHUNK_SIZE) else chunks.get(((chunk.xo*CHUNK_SIZE+new_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+new_y) // CHUNK_SIZE), dummy_chunk).prev[new_y % CHUNK_SIZE, new_x % CHUNK_SIZE]"
    set_cell_lambda = """
                        new_chunk = chunk if 0 <= {new_x} < CHUNK_SIZE and 0 <= {new_y} else chunks.get(((chunk.xo*CHUNK_SIZE+{new_x}) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+{new_y}) // CHUNK_SIZE), dummy_chunk)
                        ly, lx = {new_y}, {new_x}
                        if new_chunk != chunk:
                            ly, lx = {new_y} % CHUNK_SIZE, {new_x} % CHUNK_SIZE
                        new_chunk.data[ly, lx] = {value}
                        new_chunk.visited.add((lx, ly))
    """
    is_visited_lambda = "((new_x,new_y) in chunk.visited if 0 <= new_x < CHUNK_SIZE and 0 <= new_y else (new_x % CHUNK_SIZE, new_y % CHUNK_SIZE) in chunks.get(((chunk.xo*CHUNK_SIZE+new_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+new_y) // CHUNK_SIZE), dummy_chunk).visited)"

    result += file_header
    for index, powder in types.items():
        result += f"def powder_{index}(chunk, x: int, y: int):"
        result += func_header.format(id=index)
        result += """
    if chunk.ticks % 2 == 0:
        """
        for offset in powder.fall_offsets:
            result += func_middle.format(prob=offset[2],x=offset[0],y=offset[1], get_cell_inline=get_cell_lambda,
                                         set_cell_inline=set_cell_lambda.format(new_x="x", new_y="y",
                                                                                  value="interaction[0]"),
                                         set_cell_inline_new=set_cell_lambda.format(new_x="new_x", new_y="new_y",
                                                                                  value="interaction[1]"),
                                         interaction_index=2 if offset[1] != 0 else 3,
                                         is_visited_inline=is_visited_lambda,
                                         )
        result += """
    else:
"""
        for i in range(len(powder.fall_offsets)):
            offset = powder.fall_offsets[i if i == 0 else -i]
            result += func_middle.format(prob=offset[2],x=offset[0],y=offset[1], get_cell_inline=get_cell_lambda,
                                         set_cell_inline=set_cell_lambda.format(new_x="x", new_y="y",
                                                                                value="interaction[0]"),
                                         set_cell_inline_new=set_cell_lambda.format(new_x="new_x", new_y="new_y",
                                                                                    value="interaction[1]"),
                                         interaction_index=2 if offset[1] != 0 else 3,
                                         is_visited_inline=is_visited_lambda,
                                         )
        result += func_bottom
        result += "\n\n"

    result = result.replace("CHUNK_SIZE", str(mainloop.CHUNK_SIZE))
    with open("_unrolled.py", "w+") as f:
        f.write(result)

    global imported
    imported = importlib.import_module("_unrolled")
    imported.types = types
    imported.chunks = chunk_manager.chunks
    #imported.csize = mainloop.CHUNK_SIZE
    imported.dummy_chunk = chunk_manager.dummy_chunk
    for index in types:
        element_calls[index] = getattr(imported, f"powder_{index}")





types = {
    1: Powder(index=1,
            fall_offsets=[(0,-1,100),(-1,-1,50),(1,-1,50)],
            #mix_with_types={0: (100,100), 2: (20,20)},
            interact_with_types={0: (0, 1, 100, 100), 2:(2, 1, 50, 20)}),
    2: Powder(index=2,
              fall_offsets=[(0, -1, 100), (-1, 0, 50), (1, 0, 50)],
              #mix_with_types={0: (100,100)},
              interact_with_types={0: (0, 2, 100, 100)})

}



clears = {}
def _ready() -> None:
    create_unrolled()