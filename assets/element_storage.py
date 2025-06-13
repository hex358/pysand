TAGS = ["--no-processing"]
USE_MODULES = ["chunk_manager", "mainloop"]
modules_dict = {}
chunk_manager = None
mainloop = None
import textwrap

import sys
element_calls = {}


class PowderTags:
    Default = 0
    Liquid = 1
    Gas = 2


def build_classes():
    for powder in types.values():
        powder.bind_interactions()
    for powder in types.values():
        powder.create_interactions()

gases: set = {0, 6}
liquids: set = {2, 5}
class Powder:
    #index: int = 1
    gas_tuples = {gas: (gas, -1, 100) for gas in gases}
    liquid_tuples = {liquid: (liquid, -1, None) for liquid in liquids}
    class_tag_interactions = {
        PowderTags.Default:
            {**liquid_tuples, **gas_tuples },
        PowderTags.Liquid:
            {**liquid_tuples, **gas_tuples },
        PowderTags.Gas:
            {**liquid_tuples, **gas_tuples}
    }

    def bind_interactions(self):
        for other_type, interaction in self.enq_add_interactions.items():
            self.add_interactions[other_type] = interaction[:3]
            if interaction[3]:
                types[other_type].add_interactions[self.index] = (interaction[1], interaction[0], interaction[2])
                print((interaction[1], interaction[0], interaction[2]))

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

            if new_interaction[0] == -1: new_interaction[0] = self.index
            if new_interaction[1] == -1: new_interaction[1] = self.index
            if new_interaction[2] is None:
                new_interaction[2] = self.density - types[other_type].density

            self.interact_with_types[other_type] = tuple(new_interaction)
        self.interact_with_types.update(self.add_interactions)
        #print(self.interact_with_types)

    def __init__(self, index: int,
                 class_tags: list = [PowderTags.Default],
                 gravity_direction: int = -1,
                 fall_direction: int = -1,
                 move_probability: int = 50,
                 custom_interactions = {},
                 add_fall_offsets = [],
                 density: int = 100):
        self.interact_with_types = {}
        self.class_tags = class_tags
        self.index = index
        self.density = density
        self.fall_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability),(1,fall_direction,move_probability)]
        self.fall_offsets += add_fall_offsets
        self.enq_add_interactions = custom_interactions
        self.add_interactions = {}



types = {
    1: Powder(index=1,
            gravity_direction=-1,
            fall_direction=-1,
            density=90,
            move_probability=50),
    2: Powder(index=2,
            density=20,
            class_tags=[PowderTags.Liquid],
            fall_direction=0),
    5: Powder(index=5,
            density=87,
            class_tags=[PowderTags.Liquid],
            move_probability=30,
            custom_interactions={2: (5, 6, 100, True)},
            fall_direction=0),
    6: Powder(index=6,
            density=0,
            class_tags=[PowderTags.Gas],
            move_probability=70,
            fall_direction=0,
            gravity_direction=1),
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