import importlib
import textwrap

chunk_manager = None
imported = None
types = None

file_header = """from random import random, randint, randrange
dummy_chunk = None
chunks = None
"""

func_header = """
powder = types[{id}]
id = {id}
sleep: bool = True
keep = True
iter_counter: int = 0

    """

throw_dice_distinct = """
a = randrange(1, {max})
r = randrange(1, {max}-1)
b = r + (r >= a)
c = {total_sum} - a - b

a -= 1; b -= 1; c -=1
"""

func_middle = """
if keep:
    new_x, new_y = x + {x}, y + {y}
    if {is_visited_inline}:
        bottom_cell = {get_cell_inline}
        if bottom_cell in powder.interact_with_types:
            interaction = powder.interact_with_types[bottom_cell]
            if {prob_eval} (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                {set_cell_inline}
                {set_cell_inline_new}
            sleep = False
            keep = False
{insert}

    """

func_bottom = """
if sleep:
    chunk.skip_over()
else:
    chunk.keep_alive(and_neighbours=True)
    """

get_cell_lambda = "chunk.prev[new_y*CHUNK_SIZE+new_x] if (0 <= new_x < CHUNK_SIZE and 0 <= new_y < CHUNK_SIZE) else chunks.get(((chunk.xo*CHUNK_SIZE+new_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+new_y) // CHUNK_SIZE), dummy_chunk).prev[(new_y % CHUNK_SIZE) * CHUNK_SIZE + new_x % CHUNK_SIZE]"
set_cell_lambda = """
if {cond}:
    new_chunk = chunk if 0 <= {new_x} < CHUNK_SIZE and 0 <= {new_y} < CHUNK_SIZE else chunks.get(((chunk.xo*CHUNK_SIZE+{new_x}) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+{new_y}) // CHUNK_SIZE), dummy_chunk)
    ly, lx = {new_y}, {new_x}
    if new_chunk != chunk:
        ly, lx = {new_y} % CHUNK_SIZE, {new_x} % CHUNK_SIZE
    new_chunk.data[ly*CHUNK_SIZE + lx] = {value}
    if new_chunk != dummy_chunk:
        new_chunk.visited.add((lx, ly))
    """
is_visited_lambda = "not ((new_x,new_y) in chunk.visited if 0 <= new_x < CHUNK_SIZE and 0 <= new_y < CHUNK_SIZE else (new_x % CHUNK_SIZE, new_y % CHUNK_SIZE) in chunks.get(((chunk.xo*CHUNK_SIZE+new_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+new_y) // CHUNK_SIZE), dummy_chunk).visited)"

def indent(text: str, count: int = 1):
    for _ in range(count):
        text = text.replace('\n', '\n' + (4 * ' '))
    return text


def middle_formatted(powder, offset):
    return func_middle.format(x=offset[0], y=offset[1], get_cell_inline=get_cell_lambda,
                                set_cell_inline=indent(set_cell_lambda.format(new_x="x", new_y="y",
                                                                      value="interaction[0]", cond = "interaction[0] != id"), count=4),
                                set_cell_inline_new=indent(set_cell_lambda.format(new_x="new_x", new_y="new_y",
                                                                      value="interaction[1]", cond = "True"), count=4),
                                is_visited_inline=indent(is_visited_lambda, count=2),
                                prob_eval="" if not isinstance(offset[2], str) and offset[2] >= 100
                                else f"100*random() > 100-{offset[2]} and ",
                                insert="" if not powder.throw_dice else "iter_counter += 1",

                                    )


from itertools import permutations
from math import factorial
def create_unrolled():
    result = ""

    result += file_header
    for index, powder in types.items():
        if powder.throw_dice:
            permuts = [f"\n{permut}," for permut in permutations(powder.fall_offsets)]
            result += f"permuts_{index} = (" + "".join(permuts) + ")\n"

        result += f"def powder_{index}(chunk, x: int, y: int):"
        result += indent(func_header.format(id=index))

        if powder.throw_dice:
            result += "\n" + indent("\ncurr_offsets = permuts_{index}[randint(0,{length})]".format(index = index,
                                                                                                   length=factorial(len(powder.fall_offsets))-1))

        result += indent("\nif chunk.ticks % 2 == 0:" if not powder.throw_dice else "\nif True:")
        result += "\n" + indent("\npass", 2)

        for i in range(len(powder.fall_offsets)*2 if not powder.throw_dice else len(powder.fall_offsets)):
            if i == len(powder.fall_offsets):
                result += "\n" + indent("\nelse:")
                result += "\n" + indent("\npass", 2)
            if i >= len(powder.fall_offsets): i = -(i-len(powder.fall_offsets))
            offset = powder.fall_offsets[i] if not powder.throw_dice else ("add_x", "add_y", "prob")
            if powder.throw_dice:
                result += "\n" + indent(f"\nadd_x, add_y, prob =  curr_offsets[iter_counter]", 2)
            result += indent(middle_formatted(powder, offset), 2)

        result += indent(func_bottom)
        result += "\n\n"

    result = result.replace("CHUNK_SIZE", str(chunk_manager.CHUNK_SIZE))
    with open("_unrolled.py", "w+") as f:
        f.write(result)

    global imported
    imported = importlib.import_module("_unrolled")
    imported.types = types
    imported.chunks = chunk_manager.chunks
    #imported.csize = mainloop.CHUNK_SIZE
    imported.dummy_chunk = chunk_manager.dummy_chunk

    return {index: getattr(imported, f"powder_{index}") for index in types}