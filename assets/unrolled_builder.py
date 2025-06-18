import importlib
import textwrap

pre_built = False

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
from collections import namedtuple
dummy_chunk = None
updated_this_round = set([])
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
curr_bit: int = {curr_bit}

{pre_cond}
    """

func_middle = """
if keep:
    new_x, new_y = x + {x}, y + {y}
    if (not {is_visited}(new_x, new_y) {add_cond}) and {mandatory_cond}:
        bottom_cell = {get_cell}(new_x,new_y)
        dict1, dict2 = {dict_name}[({x}, {y}, False)], {dict2} #
        bit_1 = bottom_cell >> 8
        bit_2 = bottom_cell & 0xFF if {bit_2_cond} else 0
        if bit_1 in dict1 or ({bit_2_cond} and bit_2 in dict2):
            interaction = None
            is_bit_2 = False
            if {bit_2_cond} and bit_2 in dict2:
                is_bit_2 = True
                interaction = dict2[bit_2]
            else:
                interaction = dict1[bit_1]
            if not is_bit_2 or interaction[3] != curr_bit:
                if {prob_eval} (interaction[2] >= 100 or random()*100 > 100-interaction[2]):
                    {plant_insert}
                    if interaction[5]:
                        if interaction[0] != id:
                            {set_cell}(x,y,interaction[0] << 8 | interaction[3])
                        if {set_other_cell_cond}:
                            {set_cell}(new_x,new_y,interaction[1] << 8 | interaction[4])
                    else:
                        {set_bit}(x,y,interaction[3])
                        {set_bit}(new_x,new_y,interaction[4])
                    {plant_inline_bottom}
                sleep = False
                keep = False
{insert}

    """


set_bit_inline = """
if 0 <= bit_x < CHUNK_SIZE and 0 <= bit_y < CHUNK_SIZE:
    chunk.data[bit_y*CHUNK_SIZE+bit_x] = (chunk.data[bit_y*CHUNK_SIZE+bit_x] & 0xFF00) | (bit_val & 0xFF)
else:
    gx, gy = chunk.xo * CHUNK_SIZE + bit_x, chunk.yo * CHUNK_SIZE + bit_y
    target = chunks.get((gx // CHUNK_SIZE, gy // CHUNK_SIZE), dummy_chunk)
    local_x, local_y = gx % CHUNK_SIZE, gy % CHUNK_SIZE
    target.data[local_y*CHUNK_SIZE+local_x] = (target.data[local_y*CHUNK_SIZE+local_x] & 0xFF00) | (bit_val & 0xFF)
"""


plant_inline = """
old = {get_bit}(x, y)
"""

plant_inline_bottom = """
{set_bit}(new_x, new_y, old - 1)
if old <= 0:
    sleep = True 
"""

func_bottom = """
if sleep:
    {skip_over}()
else:
    {keep_alive}()
    """


get_cell_inline = "chunk.prev[get_y*CHUNK_SIZE+get_x] if (0 <= get_x < CHUNK_SIZE and 0 <= get_y < CHUNK_SIZE) else chunks.get(((chunk.xo*CHUNK_SIZE+get_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+get_y) // CHUNK_SIZE), dummy_chunk).prev[(get_y % CHUNK_SIZE) * CHUNK_SIZE + get_x % CHUNK_SIZE]"
get_bit_inline = "chunk.prev[get_y*CHUNK_SIZE+get_x] & 0xFF if (0 <= get_x < CHUNK_SIZE and 0 <= get_y < CHUNK_SIZE) else chunks.get(((chunk.xo*CHUNK_SIZE+get_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+get_y) // CHUNK_SIZE), dummy_chunk).prev[(get_y % CHUNK_SIZE) * CHUNK_SIZE + get_x % CHUNK_SIZE] & 0xFF"


set_cell_inline = """
new_chunk = chunk if 0 <= set_x < CHUNK_SIZE and 0 <= set_y < CHUNK_SIZE else chunks.get(((chunk.xo*CHUNK_SIZE+set_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+set_y) // CHUNK_SIZE), dummy_chunk)
ly, lx = set_y, set_x
if new_chunk != chunk:
    ly, lx = set_y % CHUNK_SIZE, set_x % CHUNK_SIZE
new_chunk.data[ly*CHUNK_SIZE + lx] = set_value# << 8
new_chunk.visited.add((lx, ly))
"""
is_visited_inline = "((visited_x,visited_y) in chunk.visited if 0 <= visited_x < CHUNK_SIZE and 0 <= visited_y < CHUNK_SIZE else (visited_x % CHUNK_SIZE, visited_y % CHUNK_SIZE) in chunks.get(((chunk.xo*CHUNK_SIZE+visited_x) // CHUNK_SIZE, (chunk.yo*CHUNK_SIZE+visited_y) // CHUNK_SIZE), dummy_chunk).visited)"

keep_alive_inline = """
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
"""

skip_over_inline = """
chunk.skipped_over_count += 1
"""

class InlineFunc:
    def __init__(self, name: str, script: str, arg_names: list[str]):
        self.name, self.script, self.arg_names = name, script, arg_names
        self.inline_tag = "{" + self.name + "}"

    def inline(self, text: str):
        while self.inline_tag + "(" in text:
            start = text.find(self.inline_tag + "(")
            prefix = text[:start]
            rest = text[start + len(self.inline_tag):]

            end_args = rest.find(")")
            raw_args = rest[1:end_args]

            inlined = self.script
            for arg_name, arg_value in zip(self.arg_names, raw_args.split(",")):
                inlined = inlined.replace(arg_name, "(" + arg_value + ")")

            line_start = text.rfind('\n', 0, start) + 1
            indent_str = text[line_start:start]
            indent_count = indent_str.count(" ")//4
            inlined = indent(inlined, indent_count)

            text = prefix + inlined + rest[end_args + 1:]

        return text

funcs = {"get_cell": InlineFunc("get_cell", get_cell_inline, ["get_x", "get_y"]),
         "set_cell": InlineFunc("set_cell", set_cell_inline, ["set_x", "set_y", "set_value"]),
         "is_visited": InlineFunc("is_visited", is_visited_inline, ["visited_x", "visited_y"]),
         "keep_alive": InlineFunc("keep_alive", keep_alive_inline, []),
         "skip_over": InlineFunc("skip_over", skip_over_inline, []),
         "set_bit": InlineFunc("set_bit", set_bit_inline, ["bit_x", "bit_y", "bit_val"]),
         "get_bit": InlineFunc("get_bit", get_bit_inline, ["get_x", "get_y"]),
         }#self.skipped_over_count += 1


def indent(text: str, count: int = 1):
    for _ in range(count):
        text = text.replace('\n', '\n' + (4 * ' '))
    return text


def middle_formatted(powder, offset, cells_cached=False):
    custom_cond_formatted = inlines(powder.custom_cond)
    inlined = inlines(func_middle, get_cell_skip=cells_cached)
    set_other_cell_cond = "True"
    if cells_cached:
        inlined = inlined.replace("{get_cell}", "replaces[add_x]#")
    plant_insert = ""
    mandatory_cond = "True"
    if powder.is_plant:
        set_other_cell_cond = "old > 0"
        plant_insert = indent(inlines(plant_inline), 5)
    rep = "None"
    if powder.has_bitwise_operations:
        rep = "{dict_name}[({x}, {y}, True)]"
    inlined = inlined.replace("{dict2}", rep)
        #mandatory_cond = inlines("({get_cell}(x-1, y)) != {id} and ({get_cell}(x+1, y)) != {id}").format(
        #               id = powder.index)#,
    return inlined.format(x=offset[0], y=offset[1],
                        bit_2_cond = str(powder.has_bitwise_operations),
                        #bitwise_interaction_cond = "False" if not powder.has_bitwise_operations else "interaction[3]",

                        mandatory_cond=mandatory_cond,
                        dict_name = f"interact_{powder.index}",
                        set_other_cell_cond = set_other_cell_cond if (offset[0],offset[1] != (0,0)) else "interaction[1] != id",
                        add_cond=custom_cond_formatted,
                        prob_eval="" if not isinstance(offset[2], str) and offset[2] >= 100
                        else f"100*random() > 100-{offset[2]} and ",
                        insert="" if not powder.throw_dice else "iter_counter += 1",
                        plant_insert=plant_insert,
                        plant_inline_bottom = indent(inlines(plant_inline_bottom),5) if powder.is_plant else ""
                        )


from itertools import permutations
from math import factorial

def inlines(string: str, **kwargs):
    for inliner in funcs.values():
        if not inliner.name + "_skip" in kwargs or not kwargs[inliner.name + "_skip"]:
            string = inliner.inline(string)
    return string



def string_unroll():
    result = ""

    result += file_header
    for index in types:
        result += f"\ninteract_{index} = None\n"

    for index, powder in types.items():
        permuts = None
        pre_cond = ""
        cached = False
        if powder.throw_dice:
            permuts = list(permutations(powder.fall_offsets))
            permut_tuples = [f"\n{permut}," for permut in permuts]
            result += f"permuts_{index} = (" + "".join(permut_tuples) + ")\n"
            result += 'replaces = {-1: 0, 0: 0, 1: 0}'
        if powder.is_plant:
           pre_cond = inlines("""
cached_left, cached_up, cached_right = ({get_cell}(x-1,y+{dir})), ({get_cell}(x,y+{dir})), ({get_cell}(x+1,y+{dir}))
if (cached_left>> 8 == {id} or cached_right>> 8 == {id} or cached_up>> 8 == {id}): 
    keep = False
else:
    replaces[-1], replaces[0], replaces[1] = cached_left, cached_up, cached_right
           """).format(id=powder.index, dir=powder.gravity_direction)
           cached = True

        curr_bit = "0"
        if powder.has_bitwise_operations:
            curr_bit = inlines("({get_bit}(x,y))")
        result += f"\n\ndef powder_{index}(chunk, x: int, y: int):"
        result += indent(func_header.format(id=index, pre_cond=pre_cond, curr_bit=curr_bit))
        result += "\n" + indent("\n" + inlines(powder.custom_script)) + "\n"

        if powder.throw_dice:
            result += "\n" + indent("\ncurr_offsets = permuts_{index}[randint(0,{length})]".format(index=index,
                                                                                                   length=len(
                                                                                                       permuts) - 1))

        result += indent("\nif chunk.ticks % 2 == 0:" if not powder.throw_dice else "\nif True:")
        result += "\n" + indent("\npass", 2)

        for i in range(len(powder.fall_offsets) * 2 if not powder.throw_dice else len(powder.fall_offsets)):
            if i == len(powder.fall_offsets):
                result += "\n" + indent("\nelse:")
                result += "\n" + indent("\npass", 2)
            if i >= len(powder.fall_offsets): i = -(i - len(powder.fall_offsets))
            offset = powder.fall_offsets[i] if not powder.throw_dice else ("add_x", "add_y", "prob")
            if powder.throw_dice:
                result += "\n" + indent(f"\nadd_x, add_y, prob =  curr_offsets[iter_counter]", 2)

            result += indent(middle_formatted(powder, offset, cells_cached=cached), 2)

        result += indent(inlines(func_bottom))
        result += "\n\n"

    result = result.replace("CHUNK_SIZE", str(chunk_manager.CHUNK_SIZE))
    with open("_unrolled.py", "w+") as f:
        f.write(result)

def import_unrolled():
    if not pre_built:
        string_unroll()

    global imported
    imported = importlib.import_module("_unrolled")
    imported.types = types
    imported.chunks = chunk_manager.chunks
    for index in types:
        setattr(imported, f"interact_{index}", types[index].raw_interactions)
    #imported.csize = mainloop.CHUNK_SIZE
    imported.MAX_UPDATE_INTENSITY = chunk_manager.MAX_UPDATE_INTENSITY
    imported.dummy_chunk = chunk_manager.dummy_chunk

    return {index: getattr(imported, f"powder_{index}") for index in types if index != 0}