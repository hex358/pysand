TAGS = ["--no-processing"]
USE_MODULES = ["chunk_manager", "mainloop"]
modules_dict = {}
chunk_manager = None
mainloop = None
import textwrap

import sys
element_calls = {}

from enum import Enum
class PowderTags(Enum):
    Default = 0
    Liquid = 1
    Gas = 2

class Any(Enum):
    CurrentElement = -255

def build_classes():
    for powder in types.values():
        powder.bind_interactions()
    for powder in types.values():
        powder.create_interactions()

class Interaction:
    def __init__(self, with_powder: int | list[int], change_itself_into: int, change_other_into: int,
                 double_sided: bool = False):
        self.interactions = {}
        if with_powder is int: with_powder = [with_powder]
        # for types in with_powder:
        #     types = [types] if types <
        #     self.interactions[types]

    def bind(self):
        pass

    def to_tuples(self):
        return self.interactions


class Powder:
    all_elements: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gases: set = {0, 6}
    liquids: set = {2, 5}
    #index: int = 1
    gas_tuples = {gas: (gas, Any.CurrentElement, 100) for gas in gases}
    liquid_tuples = {liquid: (liquid, Any.CurrentElement, None) for liquid in liquids}
    class_tag_interactions = {
        PowderTags.Default:
            {**liquid_tuples, **gas_tuples },
        PowderTags.Liquid:
            {**liquid_tuples, **gas_tuples },
        PowderTags.Gas:
            {**liquid_tuples, **gas_tuples}
    }

    def bind_interactions(self):
        #print(self.index)
        for other_type, interaction in self.enq_add_interactions.items():
            self.add_interactions[other_type] = interaction[:3]
            if interaction[3]:
                types[other_type].add_interactions[self.index] = (interaction[1], interaction[0], interaction[2])
                #print((interaction[1], interaction[0], interaction[2]))

    def create_interactions(self):
        self.interact_with_types = {}

        for tag in self.class_tags:
            for other_type, interactions in Powder.class_tag_interactions[tag].items():
                if other_type == self.index: continue
                self.interact_with_types[other_type] = interactions

        for other_type, interaction in list(self.interact_with_types.items()):
            new_interaction = list(interaction)
            if other_type in types and self.density < types[other_type].density:
                self.interact_with_types.pop(other_type); continue
            if new_interaction[2] is None:
                new_interaction[2] = self.density - types[other_type].density
            self.interact_with_types[other_type] = tuple(new_interaction)

        self.interact_with_types.update(self.add_interactions)

       # print(self.interact_with_types)
        for other_type, interaction in list(self.interact_with_types.items()):
            new_interaction = list(interaction)
            if new_interaction[0] == Any.CurrentElement: new_interaction[0] = self.index
            if new_interaction[1] == Any.CurrentElement: new_interaction[1] = self.index
            if other_type is list:
                reduce: int = 0
                for i in range(len(other_type)):
                    curr = other_type[i+reduce]
                    if curr < 0:
                        self.no_interactions_with.append(-curr)
                        other_type += [opp for opp in Powder.all_elements]
                        del other_type[i+reduce]; reduce -= 1
                new_interaction = tuple(new_interaction)
                self.interact_with_types.update({list_type: new_interaction for list_type in other_type}); continue
            elif other_type < 0:
                self.no_interactions_with.append(-other_type)
                other_type = [opp for opp in Powder.all_elements]
                self.interact_with_types.update({list_type: tuple(new_interaction) for list_type in other_type})
                continue

            self.interact_with_types[other_type] = tuple(new_interaction)

        #print(self.no_interactions_with)

        for no in self.no_interactions_with:
            self.interact_with_types.pop(no)
        #print(self.interact_with_types)

    def __init__(self, index: int,
                 class_tags: list = [PowderTags.Default],
                 throw_dice: bool = False,
                 gravity_direction: int = -1,
                 fall_direction: int = -1,
                 move_probability: int = 50,
                 custom_interactions = {},
                 add_fall_offsets = [],
                 no_interactions_with = [],
                 density: int = 100):
        self.interact_with_types = {}
        self.no_interactions_with = list(no_interactions_with)
        print(no_interactions_with)
        self.class_tags = list(class_tags)
        self.throw_dice = throw_dice
        self.index = index
        self.density = density
        self.fall_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability),(1,fall_direction,move_probability)]
        self.fall_offsets += list(add_fall_offsets)
        self.enq_add_interactions = dict(custom_interactions)
        self.add_interactions = {}


name_map = {"sand": 1, "water": 2, "stone": 3, "wood": 4, "lava": 5, "vapor": 6, }
def PowderName(name: str):
    return name_map[name]


types = {
    1: Powder(index=1,
            gravity_direction=-1,
            fall_direction=-1,
            density=90,
            move_probability=50),
    2: Powder(index=2,
            density=20,
            class_tags=[PowderTags.Liquid],
            fall_direction=0,
            custom_interactions={7:(2,8,5,False)}),
    5: Powder(index=5,
            density=87,
            class_tags=[PowderTags.Liquid],
            move_probability=30,
            custom_interactions={2: (5, 6, 100, True), 4: (0, 5, 30, False)},
            fall_direction=0),
    6: Powder(index=6,
            density=0,
            class_tags=[PowderTags.Gas],
            move_probability=70,
            custom_interactions={-6: (6, 2, 100, False)},
            fall_direction=0,
            gravity_direction=1),
    7: Powder(index=7,
            gravity_direction=-1,
            fall_direction=-1,
            density=88,
            move_probability=30,
            custom_interactions={8:(7,7,2,False)}),
    8: Powder(index=8,
            gravity_direction=-1,
            fall_direction=-1,
            density=150,
            move_probability=30,
            custom_interactions={7:(8,8,0.5,False)}),
    9: Powder(index=9,
            gravity_direction=-1,
            class_tags=[],
            fall_direction=-1,
            density=150,
            move_probability=30,
            custom_interactions={7:(8,8,0.5,False)}),
}

import unrolled_builder
unrolled = None
clears = {}
def _ready() -> None:
    a = [[2,2],[1,1]]
    build_classes()
    global unrolled
    unrolled_builder.chunk_manager = chunk_manager
    unrolled_builder.types = types
    global element_calls
    element_calls = unrolled_builder.create_unrolled()