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

current = 255

def build_classes():
    for powder in types.values():
        powder.bind_interactions()
    for powder in types.values():
        powder.create_interactions()

import math
def is_negative(x): return math.copysign(1.0, x) < 0.0


name_map = {"sand": 1, "water": 2, "stone": 3, "wood": 4, "lava": 5, "vapor": 6, "dirt": 7, "wet_dirt": 8}
def PowderName(name: str):
    return name_map[name]

class Interaction:
    def __init__(self, with_powder: int | list[int],
                 change_itself_into: int,
                 change_other_into: int,
                 probability: int = 100,
                 double_sided: bool = False):
        self.interactions = {}
        self.double_sided = double_sided
        if isinstance(with_powder, int): with_powder = [with_powder]
        skip = []
        for types in with_powder:
            if is_negative(types): skip.append(-types)
            types = [types] if not is_negative(types) else [element for element in Powder.all_elements]
            for other_type in types:
                self.interactions[other_type] = (change_itself_into, change_other_into, probability)
        for key in skip:
            self.interactions.pop(key)

    def replace(self, type: int):
        for interaction in self.interactions.values():
            for i in range(len(interaction)):
                if interaction[i] == current: interaction[i] = type

    def bind(self, type: int):
        pass

    def to_tuples(self):
        return self.interactions.copy()
        # output = {}
        # for other_type, tuple_interaction in self.interactions:
        #     output[type] = (tuple_interaction[0] if tuple_interaction[0] != current else type,
        #                     tuple_interaction[1] if tuple_interaction[1] != current else type,
        #                     tuple_interaction[2] if tuple_interaction[2] is not None else types[type].density - types[other_type].density)


class Powder:
    all_elements: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gases: set = {0, 6}
    liquids: set = {2, 5}
    #index: int = 1
    gas_interactions = [Interaction(with_powder=gas, change_itself_into=gas, change_other_into=current, probability=100)
                        for gas in gases]
    liquid_interactions = [Interaction(with_powder=liquid, change_itself_into=liquid, change_other_into=current, probability=None)
                     for liquid in liquids]
    class_tag_interactions = {
        PowderTags.Default:
            [*liquid_interactions, *gas_interactions ],
        PowderTags.Liquid:
            [*liquid_interactions, *gas_interactions ],
        PowderTags.Gas:
            [*liquid_interactions, *gas_interactions ]
    }
    
    def create_interactions(self):
        self.interact_with_types = {}
        to_add_interactions: list[Interaction] = []
        for tag in self.class_tags:
            to_add_interactions += Powder.class_tag_interactions[tag]

        for interaction in to_add_interactions:
            tuples = interaction.to_tuples()
            for with_powder, tuple_interaction in tuples.items():
                new = list(tuple_interaction)
                if self.density < types[with_powder]: continue
                if new[0] == current: new[0] = self.index
                if new[1] == current: new[1] = self.index
                if new[2] is None: new[2] = self.density - types[with_powder].density
                tuples[with_powder] = tuple(new)
            self.interact_with_types |= tuples

        for interaction in self.add_interactions:
            self.interact_with_types |= interaction.to_tuples()

        if self.index == 2:
            print(self.interact_with_types)

    def bind_interactions(self):
        for interaction in self.add_interactions:
            if interaction.double_sided:
                for with_powder, interaction_tuple in interaction.to_tuples().items():
                    other_powder = types[with_powder]
                    if not self.index in other_powder.add_interactions:
                        other_powder.add_interactions[self.index] = (interaction_tuple[1], interaction_tuple[0], interaction_tuple[2])



    def __init__(self, index: int,
                 class_tags: list = [PowderTags.Default],
                 throw_dice: bool = False,
                 gravity_direction: int = -1,
                 fall_direction: int = -1,
                 move_probability: int = 50,
                 custom_interactions: list[Interaction] = {},
                 add_fall_offsets = [],
                 density: int = 100):
        self.interact_with_types = {}
        #print(no_interactions_with)
        self.class_tags = list(class_tags)
        self.throw_dice = throw_dice
        self.index = index
        self.density = density
        self.fall_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability),(1,fall_direction,move_probability)]
        self.fall_offsets += list(add_fall_offsets)
        self.add_interactions = list(custom_interactions)





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
            custom_interactions=[]),
    5: Powder(index=5,
            density=87,
            class_tags=[PowderTags.Liquid],
            move_probability=30,
            custom_interactions=[],
            fall_direction=0),
    6: Powder(index=6,
            density=0,
            class_tags=[PowderTags.Gas],
            move_probability=70,
            custom_interactions=[],
            fall_direction=0,
            gravity_direction=1),
    7: Powder(index=7,
            gravity_direction=-1,
            fall_direction=-1,
            density=88,
            move_probability=30,
            custom_interactions=[]),
    8: Powder(index=8,
            gravity_direction=-1,
            fall_direction=-1,
            density=150,
            move_probability=30,
            custom_interactions=[]),
    9: Powder(index=9,
            gravity_direction=-1,
            class_tags=[],
            fall_direction=-1,
            density=150,
            move_probability=30,
            custom_interactions=[]),
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