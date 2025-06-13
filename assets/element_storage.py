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
    Sand = 1
    Liquid = 2
    Gas = 3


def build_classes():
    for powder in types.values():
        powder.create_interactions()

class Powder:
    #index: int = 1
    class_tags = {}

    def create_interactions(self):
        self.interact_with_types = {}
        for tag in Powder.class_tags:
            self.interact_with_types.update(class_tags[tag])
        for other_type, interaction in self.interact_with_types.items():
            if interaction[0] == -1: interaction[0] = self.index
            if interaction[1] == -1: interaction[1] = self.index
            interaction[2] = self.density - types[other_type]
            interaction[3] = int(interaction[2]) * self.horizontal_damping
        self.interact_with_types.update(self.add_interactions)
        print(self.interact_with_types)

    def __init__(self, index: int,
                 class_tags: tuple = (),
                 gravity_direction: int = -1,
                 fall_direction: int = -1,
                 move_probability: int = 50,
                 add_interactions = {},
                 add_fall_offsets = (),
                 horizontal_damping = 0.2,
                 density: int = 100):
        self.interact_with_types = {}
        self.index = index
        self.density = density
        self.fall_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability),(1,fall_direction,move_probability)] + [*add_fall_offsets]
        self.add_interactions = add_interactions
        self.horizontal_damping = horizontal_damping


    #fall_offsets: list = field(default_factory=list)
    # offset: probability. All offsets except the first one will be processed in reversed order during odd-numbered ticks.

    #interact_with_types: dict = field(default_factory=dict)
    # element: itself turns into.., type turns into.., vertical interaction probability, horizontal interaction probability.




types = {
    1: Powder(index=1,
              gravity_direction=-1,
              fall_direction=-1,
              density=100,
              add_interactions={0:(0,1,100)}),
            #fall_offsets=[(0,-1,100),(-1,-1,50),(1,-1,50)],
            #interact_with_types={0: (0, 1, 100, 100), 6: (6, 1, 100, 100), 5: (5, 1, 1, 1), 2:(2, 1, 50, 20)}), # sand
    2: Powder(index=2,
              density=30),
              #fall_offsets=[(0, -1, 100), (-1, 0, 50), (1, 0, 50)],
              #interact_with_types={0: (0, 2, 100, 100), 6: (6, 2, 100, 100), 5: (6, 5, 100, 100), 7: (2, 8, 1, 1)}), # water
    5: Powder(index=5),
              #fall_offsets=[(0, -1, 100), (-1, 0, 20), (1, 0, 20)],
              #interact_with_types={0: (0, 5, 100, 100), 6: (6, 5, 100, 100), 2: (5, 6, 100, 100), 4: (0, 5, 5, 5)}), # lava
    6: Powder(index=6),
              #fall_offsets=[(0, 1, 100), (-1, 0, 60), (1, 0, 60)],
              #interact_with_types={0: (0, 6, 100, 100)}), # vapor
    7: Powder(index=7),
              #fall_offsets=[(0, -1, 100), (-1, -1, 20), (1, -1, 20)],
              #interact_with_types={0: (0, 7, 100, 100)}),  # dirt
    8: Powder(index=8)
              #fall_offsets=[(0, -1, 100), (-1, -1, 20), (1, -1, 20)],
              #interact_with_types={0: (0, 8, 100, 100), })  # grass

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