import importlib
import textwrap

chunk_manager = None
imported = None
types = None

file_header = """
############        unrolled.py        ############
# This file is created automatically to maximize  #
# the perfomance via loop unrolling and function  #
# inlining. It's not human-readable.              #
###################################################





from random import random, randint, randrange
dummy_chunk = None
chunks = None
"""

func_header = """
powder = types[{id}]
id = {id}
get_cell = chunk.get_cell
set_cell = chunk.set_cell
sleep: bool = True
keep = True
iter_counter: int = 0

    """

func_middle = """
if keep:
    new_x, new_y = x + {x}, y + {y}
    if not {is_visited}(new_x, new_y) {add_cond}:
        bottom_cell = {get_cell}(new_x,new_y)
        if bottom_cell in powder.interact_with_types:
            interaction = powder.interact_with_types[bottom_cell]
            if {prob_eval} (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                if interaction[0] != id:
                    {set_cell}(x,y,interaction[0])
                if {set_other_cell_cond}:
                    {set_cell}(new_x,new_y,interaction[1])
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


get_cell_inline = "chunk.prev[get_y*CHUNK_SIZE+get_x] if (0 <= get_x < CHUNK_SIZE and 0 <= get_y < CHUNK_SIZE) else chunks.get(((chunk.xo*CHUNK_SIZE+get_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+get_y) // CHUNK_SIZE), dummy_chunk).prev[(get_y % CHUNK_SIZE) * CHUNK_SIZE + get_x % CHUNK_SIZE]"


set_cell_inline = """
new_chunk = chunk if 0 <= set_x < CHUNK_SIZE and 0 <= set_y < CHUNK_SIZE else chunks.get(((chunk.xo*CHUNK_SIZE+set_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+set_y) // CHUNK_SIZE), dummy_chunk)
ly, lx = set_y, set_x
if new_chunk != chunk:
    ly, lx = set_y % CHUNK_SIZE, set_x % CHUNK_SIZE
new_chunk.data[ly*CHUNK_SIZE + lx] = set_value
if new_chunk != dummy_chunk:
    new_chunk.visited.add((lx, ly))
"""
is_visited_inline = "((visited_x,visited_y) in chunk.visited if 0 <= visited_x < CHUNK_SIZE and 0 <= visited_y < CHUNK_SIZE else (visited_x % CHUNK_SIZE, visited_y % CHUNK_SIZE) in chunks.get(((chunk.xo*CHUNK_SIZE+visited_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+visited_y) // CHUNK_SIZE), dummy_chunk).visited)"

keep_alive_inline = """
xo,yo = chunk.xo, chunk.yo
chunks.get((xo-1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo+1,yo), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo-1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo-1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo+1,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo+1,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo,yo-1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
chunks.get((xo,yo+1), dummy_chunk).update_intensity = MAX_UPDATE_INTENSITY
"""

skip_over_inline = """
chunk.skipped_over_count += 1
"""

class InlineFunc:
    def __init__(self, name: str, script: str, arg_names: list[str]):
        self.name, self.script, self.arg_names = name, script, arg_names

    def inline(self, text: str):
        inline_tag = "{" + self.name + "}"

        while inline_tag + "(" in text:
            start = text.find(inline_tag + "(")
            prefix = text[:start]
            rest = text[start + len(inline_tag):]

            end_args = rest.find(")")
            raw_args = rest[1:end_args]

            vals = raw_args.split(",")
            mapping = dict(zip(self.arg_names, vals))

            line_start = text.rfind('\n', 0, start) + 1
            indent_str = text[line_start:start]
            indent_count = indent_str.count(" ")//4

            inlined = self.script
            for k, v in mapping.items():
                inlined = inlined.replace(k, v)
            inlined = indent(inlined, indent_count)

            text = prefix + inlined + rest[end_args + 1:]

        return text

funcs = {"get_cell": InlineFunc("get_cell", get_cell_inline, ["get_x", "get_y"]),
         "set_cell": InlineFunc("set_cell", set_cell_inline, ["set_x", "set_y", "set_value"]),
         "is_visited": InlineFunc("is_visited", is_visited_inline, ["visited_x", "visited_y"]),
         "keep_alive": InlineFunc("keep_alive", keep_alive_inline, []),
         "skip_over": InlineFunc("skip_over", skip_over_inline, [])}#self.skipped_over_count += 1


def indent(text: str, count: int = 1):
    for _ in range(count):
        text = text.replace('\n', '\n' + (4 * ' '))
    return text


def middle_formatted(powder, offset):
    custom_cond_formatted = inlines(powder.custom_cond)
    inlined = inlines(func_middle)
    return inlined.format(x=offset[0], y=offset[1],
                        set_other_cell_cond = "True" if (offset[0],offset[1] != (0,0)) else "interaction[1] != id",
                        add_cond=custom_cond_formatted,
                        prob_eval="" if not isinstance(offset[2], str) and offset[2] >= 100
                        else f"100*random() > 100-{offset[2]} and ",
                        insert="" if not powder.throw_dice else "iter_counter += 1",
                        )


from itertools import permutations
from math import factorial

def inlines(string: str):
    for func_name, inliner in funcs.items():
        string = inliner.inline(string)
    return string

def create_unrolled():
    result = ""

    result += file_header
    for index, powder in types.items():
        permuts = None
        if powder.throw_dice:
            permuts = list(permutations(powder.fall_offsets))
            permut_tuples = [f"\n{permut}," for permut in permuts]
            result += f"permuts_{index} = (" + "".join(permut_tuples) + ")\n"

        result += f"def powder_{index}(chunk, x: int, y: int):"
        result += indent(func_header.format(id=index))
        result += "\n"+indent("\n"+inlines(powder.custom_script))+"\n"

        if powder.throw_dice:
            result += "\n" + indent("\ncurr_offsets = permuts_{index}[randint(0,{length})]".format(index = index,
                                                                                                   length = len(permuts)-1))

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

        result += indent(inlines(func_bottom))
        result += "\n\n"

    result = result.replace("CHUNK_SIZE", str(chunk_manager.CHUNK_SIZE))
    with open("_unrolled.py", "w+") as f:
        f.write(result)

    global imported
    imported = importlib.import_module("_unrolled")
    imported.types = types
    imported.chunks = chunk_manager.chunks
    #imported.csize = mainloop.CHUNK_SIZE
    imported.MAX_UPDATE_INTENSITY = chunk_manager.MAX_UPDATE_INTENSITY
    imported.dummy_chunk = chunk_manager.dummy_chunk

    return {index: getattr(imported, f"powder_{index}") for index in types if index != 0}