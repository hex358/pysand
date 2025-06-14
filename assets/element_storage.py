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


other = 254
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
                 itself_turns_into: int,
                 other_turns_into: int,
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
                self.interactions[other_type] = (itself_turns_into if itself_turns_into != other else other_type,
                                                 other_turns_into if other_turns_into != other else other_type, probability)
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

class Powder:
    all_elements: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gases: set = {0, 6}
    liquids: set = {2, 5}
    #index: int = 1
    gas_interactions = [Interaction(with_powder=gas, itself_turns_into=gas, other_turns_into=current, probability=None)
                        for gas in gases]
    liquid_interactions = [Interaction(with_powder=liquid, itself_turns_into=liquid, other_turns_into=current, probability=None)
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
        add = 100 if self.gravity_direction == 1 else 0

        for tag in self.class_tags:
            to_add_interactions += Powder.class_tag_interactions[tag]

        for interaction in to_add_interactions:
            tuples = {}
            for with_powder, tuple_interaction in interaction.to_tuples().items():
                new = list(tuple_interaction)

                if new[2] is None: new[2] = add + -self.gravity_direction * (self.density - types[with_powder].density)
                if with_powder in types and self.density < types[with_powder].density: continue
                if with_powder == self.index: continue
                if new[0] == current: new[0] = self.index
                if new[1] == current: new[1] = self.index

                tuples[with_powder] = tuple(new)
            self.interact_with_types |= tuples

        for interaction in self.add_interactions.values():
            self.interact_with_types |= interaction.to_tuples()

    def bind_interactions(self):
        for interaction in list(self.add_interactions.values()):
            #print(interaction.to_tuples())
            if interaction.double_sided:
                for with_powder, interaction_tuple in interaction.to_tuples().items():
                    other_powder = types[with_powder]
                    if not self.index in other_powder.add_interactions:
                        other_powder.add_interactions[self.index] = Interaction(self.index, interaction_tuple[1], interaction_tuple[0], interaction_tuple[2])



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
        self.gravity_direction = gravity_direction
        self.class_tags = list(class_tags)
        self.throw_dice = throw_dice
        self.index = index
        self.density = density
        self.fall_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability),(1,fall_direction,move_probability)]
        self.fall_offsets += list(add_fall_offsets)
        self.add_interactions = {}
        for interaction in custom_interactions:
            self.add_interactions |= {_tuple[0]: interaction for _tuple in interaction.to_tuples().values()}




types = {
    0: Powder(index=0,
                gravity_direction=-1,
                class_tags=[],
                fall_direction=-1,
                density=-100,
                move_probability=50),
    1: Powder(index=1,
                gravity_direction=-1,
                fall_direction=-1,
                density=90,
                move_probability=50),
    2: Powder(index=2,
                density=20,
                class_tags=[PowderTags.Liquid],
                fall_direction=0,
                custom_interactions=[Interaction(with_powder=5, double_sided=True, itself_turns_into=6, other_turns_into=5),
                                     Interaction(with_powder=7, itself_turns_into=2, other_turns_into=8, probability=20)]),
    5: Powder(index=5,
                density=87,
                class_tags=[PowderTags.Liquid],
                move_probability=30,
                custom_interactions=[],
                fall_direction=0),
    6: Powder(index=6,
                density=-70,
                class_tags=[PowderTags.Gas],
                move_probability=50,
                custom_interactions=[],
                fall_direction=0,
                gravity_direction=1),
    7: Powder(index=7,
                gravity_direction=-1,
                fall_direction=-1,
                density=87,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=8, itself_turns_into=7, other_turns_into=7, probability=4)]),
    8: Powder(index=8,
                gravity_direction=-1,
                fall_direction=-1,
                density=100,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=7, itself_turns_into=8, other_turns_into=8, probability=0.5)]),
    9: Powder(index=9,
                gravity_direction=1,
                class_tags=[],
                fall_direction=1,
                density=150,
                throw_dice=True,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=0, itself_turns_into=9, other_turns_into=9, probability=1)]),
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