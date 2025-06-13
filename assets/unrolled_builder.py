import importlib
import textwrap

chunk_manager = None
imported = None
types = None

file_header = """from random import random
dummy_chunk = None
chunks = None
"""

func_header = """
powder = types[{id}]
sleep: bool = True
keep = True

    """

func_middle = """
if keep:
    new_x, new_y = x + {x}, y + {y}
    if {is_visited_inline}:
        bottom_cell = {get_cell_inline}
        if bottom_cell in powder.interact_with_types:
            interaction = powder.interact_with_types[bottom_cell] #(move_probability == 100 or random()*100 > 100-move_probability) 
            if {prob_eval} (interaction[{interaction_index}] == 100 or random()*100 > 100-interaction[{interaction_index}]):
                {set_cell_inline}
                {set_cell_inline_new}
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
new_chunk = chunk if 0 <= {new_x} < CHUNK_SIZE and 0 <= {new_y} < CHUNK_SIZE else chunks.get(((chunk.xo*CHUNK_SIZE+{new_x}) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+{new_y}) // CHUNK_SIZE), dummy_chunk)
ly, lx = {new_y}, {new_x}
if new_chunk != chunk:
    ly, lx = {new_y} % CHUNK_SIZE, {new_x} % CHUNK_SIZE
new_chunk.data[ly, lx] = {value}
if new_chunk != dummy_chunk:
    new_chunk.visited.add((lx, ly))
    """
is_visited_lambda = "not ((new_x,new_y) in chunk.visited if 0 <= new_x < CHUNK_SIZE and 0 <= new_y < CHUNK_SIZE else (new_x % CHUNK_SIZE, new_y % CHUNK_SIZE) in chunks.get(((chunk.xo*CHUNK_SIZE+new_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+new_y) // CHUNK_SIZE), dummy_chunk).visited)"

def indent(text: str, count: int = 1):
    for _ in range(count):
        text = text.replace('\n', '\n' + (4 * ' '))
    return text

def create_unrolled():
    result = ""

    result += file_header
    for index, powder in types.items():
        result += f"def powder_{index}(chunk, x: int, y: int):"
        result += indent(func_header.format(id=index))
        result += indent("\nif chunk.ticks % 2 == 0:")
        result += "\n" + indent("\npass", 2)
        for i in range(len(powder.fall_offsets)*2):
            if i == len(powder.fall_offsets):
                result += "\n" + indent("\nelse:")
                result += "\n" + indent("\npass", 2)
            if i >= len(powder.fall_offsets): i = -(i-len(powder.fall_offsets))
            offset = powder.fall_offsets[i]
            block = func_middle.format(x=offset[0], y=offset[1], get_cell_inline=get_cell_lambda,
                                         set_cell_inline=indent(set_cell_lambda.format(new_x="x", new_y="y",
                                                                                  value="interaction[0]"), count=4),
                                         set_cell_inline_new=indent(set_cell_lambda.format(new_x="new_x", new_y="new_y",
                                                                                  value="interaction[1]"), count=4),
                                         interaction_index=2 if offset[1] != 0 else 3,
                                         is_visited_inline=indent(is_visited_lambda, count=2),
                                         prob_eval="" if offset[2] == 100 else f"100*random() > 100-{offset[2]} and "
                                         )
            result += indent(block, 2)

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