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
    Plant = 3


other = 254
current = 255

def clear():
    unrolled_builder.imported.updated_this_round.clear()

def build_classes():
    for powder in types.values():
        powder.bind_interactions()
    for powder in types.values():
        powder.create_interactions()

import math
def is_negative(x): return math.copysign(1.0, x) < 0.0


name_map = {"sand": 1, "water": 2, "stone": 3, "wood": 4, "lava": 5, "vapor": 6, "dirt": 7, "wet_dirt": 8, "grass": 9}
def PowderName(name: str):
    return name_map[name]


from collections import namedtuple
class Interaction:
    def __init__(self, with_powder: int | list[int] = None,
                 itself_turns_into: int = None,
                 other_turns_into: int = None,
                 probability: int = 100,
                 double_sided: bool = False,
                 in_offsets: list[tuple[int, int]] = None,
                 itself_bit_state: int = 0,
                 other_bit_state: int = 0,
                 with_bit: int | list[int] = None,
                 on_ground_touch: bool = False,
                 if_bit_state_is: int | list[int] = None
                 ):
        self.interactions = {}
        self.double_sided = double_sided
        if if_bit_state_is is None: if_bit_state_is = list(range(0,256))
        if isinstance(if_bit_state_is, int): if_bit_state_is = [if_bit_state_is]
        is_bit_interaction = not with_bit is None
        if in_offsets is None: in_offsets = []

        self.is_with_bit = is_bit_interaction
        self.in_offsets = in_offsets
        if with_bit is not None: with_powder = with_bit
        if isinstance(with_powder, int): with_powder = [with_powder]

        skip = []
        for types in with_powder:
            if is_negative(types): skip.append(-types)

        for types in with_powder:
            types = [types]# if not is_negative(types) else [element for element in Powder.all_elements]
            for other_type in types:
                if other_type in skip or -other_type in skip: continue
                self.interactions[(other_type, tuple(in_offsets), is_bit_interaction)] = (itself_turns_into if itself_turns_into != other else other_type,
                                                                            other_turns_into if other_turns_into != other else other_type,
                                                                            probability,
                                                                            in_offsets,
                                                                            itself_bit_state if itself_bit_state != other else other_type,
                                                                            other_bit_state if other_bit_state != other else other_type,
                                                                            is_bit_interaction,
                                                                            on_ground_touch,
                                                                            set(if_bit_state_is))
       # if -9 in with_powder:
     #       print(self.interactions)
        # if self.is_with_bit:
        #     print(with_powder)
        #     print(self.interactions)

    def replace(self, type: int):
        for interaction in self.interactions.values():
            for i in range(len(interaction)):
                if interaction[i] == current: interaction[i] = type

    def bind(self, type: int):
        pass

    def to_tuples(self):
        return self.interactions.copy()

class Powder:
    all_elements: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99]
    bit_states: list = list(range(0,256))
    gases: set = {0, 6}
    liquids: set = {2, 5}
    solids: list = [1, 3, 4, 7, 8, 9, 10, 99]
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
            [*liquid_interactions, *gas_interactions ],
        PowderTags.Plant:
            []
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

                if new[2] is None: new[2] = add + -self.gravity_direction * (self.density - types[with_powder[0]].density)
                if with_powder in types and self.density < types[with_powder[0]].density: continue
                if with_powder == self.index: continue
                if new[0] == current: new[0] = self.index
                if new[1] == current: new[1] = self.index

                tuples[with_powder] = tuple(new)
            self.interact_with_types |= tuples

        for interaction in self.add_interactions.values():
            self.interact_with_types |= interaction.to_tuples()

        self.raw_interactions = {(offset[0], offset[1], True): {} for offset in self.fall_offsets}
        self.raw_interactions |= {(offset[0], offset[1], False): {} for offset in self.fall_offsets}
        for with_type, interaction in self.interact_with_types.items():
            if with_type[2]: self.has_bitwise_operations = True
            if with_type[0] == self.index: continue
            offsets = []
            if not interaction[3]:
                offsets = self.fall_offsets
            else:
                offsets = interaction[3]
            for offset in offsets:
                if offset in self.interaction_checks: continue
                self.raw_interactions[(offset[0], offset[1], with_type[2])][with_type[0]] = (
                interaction[0], interaction[1], interaction[2], interaction[4], interaction[5], interaction[0] is not None, interaction[8])
        #print(self.raw_interactions)

    def bind_interactions(self):
        for interaction in list(self.add_interactions.values()):
            #print(interaction.to_tuples())
            if interaction.double_sided and not interaction.is_with_bit:
                for with_powder, interaction_tuple in interaction.to_tuples().items():
                    other_powder = types[with_powder[0]]
                    if not self.index in other_powder.add_interactions:
                        other_powder.add_interactions[(self.index, ())] = Interaction(self.index, interaction_tuple[1], interaction_tuple[0], interaction_tuple[2],
                                                                                itself_bit_state=interaction_tuple[5], other_bit_state=interaction_tuple[4])



    def __init__(self, index: int,
                 class_tags: list = [PowderTags.Default],
                 throw_dice: bool = False,
                 gravity_direction: int = -1,
                 fall_direction: int = -1,
                 move_probability: int = 50,
                 custom_interactions: list[Interaction] = {},
                 custom_scipt = "",
                 custom_cond = "",
                 add_interaction_checks = [],
                 add_fall_offsets = [],
                 density: int = 100):
        self.raw_interactions = {}
        self.interact_with_types = {}
        self.is_plant = False
        self.has_bitwise_operations = False
        #print(no_interactions_with)
        self.custom_script, self.custom_cond = custom_scipt, custom_cond
        self.gravity_direction = gravity_direction
        self.class_tags = list(class_tags)
        self.throw_dice = throw_dice
        self.index = index
        self.density = density

        self.interaction_checks = set(add_interaction_checks)
        add_fall_offsets += add_interaction_checks

        default_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability), (1,fall_direction,move_probability)]
        offsets_dict = dict({offset[0:2]: offset for offset in default_offsets})
        offsets_dict |= dict({offset[0:2]: offset for offset in add_fall_offsets})
        self.fall_offsets = []
        for offset in offsets_dict.values():
            if offset[2] > 0:
                self.fall_offsets.append(offset)

        self.add_interactions = {}
        for interaction in custom_interactions:
            self.add_interactions |= {key: interaction for key, _tuple in interaction.to_tuples().items()}

plant_heights = {}
class Plant(Powder):
    def __init__(self, index: int,
                 growth_direction: int = 1,
                 growth_probability: int = 20,
                 growth_suitable: list[int] = [],
                 branch_probability: int = 5,
                 height: int = 10):
        super().__init__(index,
                        class_tags=[PowderTags.Plant],
                        throw_dice=True,
                        gravity_direction=growth_direction,
                        fall_direction=growth_direction,
                        add_fall_offsets=[(-1,growth_direction, branch_probability),
                                          (1, growth_direction, branch_probability),
                                          (0, growth_direction, growth_probability)
                                          ],
                        )
        self.is_plant = True
        plant_heights[index] = height
        self.height = height
        for gas in growth_suitable:
            self.add_interactions[gas] = Interaction(with_powder=gas, itself_turns_into=index, other_turns_into=index, probability=100)



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
                density=80,
                move_probability=50),
    2: Powder(index=2,
                density=40,
                class_tags=[PowderTags.Liquid],
                fall_direction=0,
                custom_interactions=[Interaction(with_powder=5, double_sided=True, itself_turns_into=6, other_turns_into=5),
                                     Interaction(with_powder=7, itself_turns_into=2, other_turns_into=8, probability=100, double_sided=True)]),
    5: Powder(index=5,
                density=70,
                class_tags=[PowderTags.Liquid],
                move_probability=30,
                custom_interactions=[Interaction(with_powder=4, itself_turns_into=0, other_turns_into=5, probability=30),
                                     Interaction(with_powder=8, itself_turns_into=5, other_turns_into=7, probability=4)],
                fall_direction=0),
    6: Powder(index=6,
                density=-100,
                class_tags=[PowderTags.Gas],
                move_probability=50,
                custom_interactions=[],
                fall_direction=0,
                gravity_direction=1),
    7: Powder(index=7,
                gravity_direction=-1,
                fall_direction=-1,
                density=80,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=8, itself_turns_into=7, other_turns_into=7, probability=11, double_sided=True)]),
    8: Powder(index=8,
                gravity_direction=-1,
                fall_direction=-1,
                density=120,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=7, itself_turns_into=8, other_turns_into=8, probability=10.9)],
                ),
    9: Powder(index=9,
                gravity_direction=-1,
                fall_direction=-1,
                density=120,
                move_probability=50,
                add_interaction_checks=[(0,1,100)],
                custom_interactions=[#Interaction(with_powder=Powder.gases, itself_turns_into=10, other_turns_into=other, probability=0,
                                    #            itself_bit_state=20, in_offsets=[(0,1)]),
                                     Interaction(itself_turns_into=None, other_turns_into=None, probability=100,
                                                in_offsets=[(0,-1)],
                                                itself_bit_state=1,other_bit_state=1,with_bit=1),
                                     Interaction(with_powder=Powder.solids+[-9], itself_turns_into=None, other_turns_into=None,
                                                 probability=100,
                                                 in_offsets=[(0, -1)],
                                                 itself_bit_state=1, other_bit_state=1, if_bit_state_is=0),
                                    Interaction(with_powder=Powder.gases, itself_turns_into=10, other_turns_into=other,
                                                probability=0.5,
                                                in_offsets=[(0, 1)],
                                                itself_bit_state=10, other_bit_state=1, if_bit_state_is=1),

                                    ]
                ),
    10: Plant(index=10,
                growth_direction=1,
                branch_probability=15,
                growth_probability=100,
                growth_suitable=[0],
                height=10,
                )
}

import assets.unrolled_builder as unrolled_builder
unrolled = None
clears = {}
def _ready() -> None:
    build_classes()
    global unrolled
    unrolled_builder.chunk_manager = chunk_manager
    unrolled_builder.types = types
    global element_calls
    del types[0]
    element_calls = unrolled_builder.import_unrolled()