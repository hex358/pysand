TAGS = ["--no-processing"]
USE_MODULES = ["chunk_manager", "mainloop", "render", "ui"]
modules_dict = {}
chunk_manager = None
ui = None
render = None
mainloop = None
import logging
import textwrap

import sys
element_calls = {}

obtainable = []

from enum import Enum
class PowderTags(Enum):
    Default = 1
    Liquid = 2
    Gas = 4
    Plant = 8
    Hot = 16
    Fire = 32

class Keywords(Enum):
    burn_prob = 256
    temp_burn = 257
    temp_corrode = 258
    density_diff = 259
    other = 260
    current = 261
    swap = 262
    evaporate = 263


def clear():
    unrolled_builder.imported.updated_this_round.clear()

def build_classes():
    for powder in types.values():
        for tag in powder.class_tags:
            powder.to_add_interactions += Powder.class_tag_interactions[tag]
    for powder in types.values():
        if isinstance(powder, StablePowder): continue
        powder.bind_interactions()
    for powder in types.values():
        if isinstance(powder, StablePowder): continue
        powder.create_interactions()

import math
def is_negative(x):
    return math.copysign(1.0, x) < 0.0


name_map = {"sand": 1, "water": 2, "stone": 3, "wood": 4, "lava": 5, "vapor": 6, "dirt": 7, "wet_dirt": 8, "grass": 9}
def PowderName(name: str):
    return name_map[name]

from collections import namedtuple


class BitRelative:
    def __init__(self, value: int, relative_to_itself = True):
        self.value = value
        self.relative_to_itself = relative_to_itself



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
                 if_bit_state_is: int | list[int] = None,
                 change_itself_bit: BitRelative = None,
                 change_other_bit: BitRelative = None,
                 expand: bool = False,
                 prioritized: bool = False,
                 tick_modulus: int = 1,

                 ):
        self.interactions = {}
        self.double_sided = double_sided
        self.prioritized = prioritized
        #if if_bit_state_is is None: if_bit_state_is = list(range(0,256))
        if not isinstance(if_bit_state_is, list): if_bit_state_is = [if_bit_state_is]

        is_bit_interaction = not with_bit is None
        if in_offsets is None: in_offsets = []

        self.is_with_bit = is_bit_interaction
        self.with_powder = with_powder
        self.in_offsets = in_offsets

        with_bits = [with_bit] if isinstance(with_bit, int) or with_bit is None else with_bit
        #if with_bit is not None: with_powder = with_bit
        with_powder = [with_powder] if isinstance(with_powder, int) or with_powder is None else with_powder

        skip = []
        for powder in with_powder:
            if is_negative(powder): skip.append(-powder)

        for other_type in with_powder:
          #  if other_type == 9:
           #     print(if_bit_state_is)
            if other_type in skip or -other_type in skip: continue
            for other_bit in with_bits:
                new_tuple = (itself_turns_into if itself_turns_into != Keywords.other else other_type,
                            other_turns_into if other_turns_into != Keywords.other else other_type,
                            probability,
                            in_offsets,
                            itself_bit_state if itself_bit_state != Keywords.other else other_bit,
                            other_bit_state if other_bit_state != Keywords.other else other_bit,
                            is_bit_interaction,
                            if_bit_state_is,
                            change_itself_bit,
                            change_other_bit,
                            expand,
                            prioritized,
                            tick_modulus
                            )

                self.interactions[(other_type, other_bit, is_bit_interaction, tuple(in_offsets), tuple(if_bit_state_is))] = new_tuple



    def to_tuples(self):
        return self.interactions.copy()

update_types = {}

class SubPowder:
    def __init__(self, bit_interactions, id_space):
        self.bit_interactions = bit_interactions
        self.id_space = id_space


all_elements: list = None
gases: set = None
fires: set = None
liquids: set = None
solids: list = None
meltables: list = None
flammables: list = None
hot: list = None

# all_elements: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 99]
# gases: set = {0, 6}
# fires: set = {11}
# liquids: set = {2, 5}
# solids: list = [1, 3, 4, 7, 8, 9, 99]
# meltables: list = [2]
# flammables: list = [4, 9, 10, 12]
# hot: list = [5, 11]

class Powder:


    all_elements: list = None
    gases: set = None
    fires: set = None
    liquids: set = None
    solids: list = None
    meltables: list = None
    flammables: list = None
    hot: list = None
    #index: int = 1
    class_tag_interactions = {}

    @staticmethod
    def initialize():
        print("AA")
        gas_interactions = [Interaction(with_powder=gas, itself_turns_into=gas, other_turns_into=Keywords.current, probability=Keywords.density_diff)
                            for gas in gases]
        liquid_interactions = [Interaction(with_powder=liquid, itself_turns_into=liquid, other_turns_into=Keywords.current, probability=Keywords.density_diff)
                         for liquid in liquids]
        fire_interactions = [Interaction(with_powder=fire, itself_turns_into=fire, other_turns_into=Keywords.current, probability=100)
                         for fire in fires]
        Powder.class_tag_interactions = {
            PowderTags.Default:
                [*liquid_interactions, *gas_interactions, *fire_interactions ],
            PowderTags.Liquid:
                [*liquid_interactions, *gas_interactions, *fire_interactions ],
            PowderTags.Gas:
                [*gas_interactions],#, *gas_interactions ],
            PowderTags.Plant:
                [],
            PowderTags.Fire:
                [Interaction(with_powder=flammables, itself_turns_into=Keywords.current, other_turns_into=Keywords.current, probability=Keywords.temp_burn, itself_bit_state=0,
                prioritized=True,
                expand=True),
                 Interaction(with_powder=meltables, itself_turns_into=Keywords.evaporate, other_turns_into=Keywords.current,
                             probability=Keywords.temp_corrode)
                 ],
            PowderTags.Hot:
                [Interaction(with_powder=meltables, itself_turns_into=Keywords.evaporate, other_turns_into=Keywords.current, probability=Keywords.temp_corrode),
                 Interaction(with_powder=flammables, itself_turns_into=Keywords.current, other_turns_into=11,
                             probability=Keywords.temp_burn, expand=True),
                 ],
        }

    def prob_eval(self, prob: float, other_powder: "Powder") -> float:
        add = 100 if self.gravity_direction == 1 else 0
        match prob:
            case Keywords.density_diff:
                prob = add + -self.gravity_direction * (self.density - other_powder.density)
            case Keywords.temp_corrode:
                other = other_powder.meltability
                prob = self.temperature * other / 100.0
            case Keywords.temp_burn:
                prob = self.temperature * other_powder.flammability / 100.0
        return prob

    def create_interactions(self):
        if self.index == 0: return

        self.interact_with_types = {}
        to_add_interactions = self.to_add_interactions

        if self.index in Powder.meltables:
            for powder in Powder.hot:
                to_add_interactions.append(Interaction(
                    with_powder=powder, probability=Powder.prob_eval(types[powder], Keywords.temp_corrode, self, ),
                    itself_turns_into=self.evaporates_into, other_turns_into=powder
                ))

        for interaction in to_add_interactions:
            tuples = {}
            for tuple_key, tuple_interaction in list(interaction.to_tuples().items()):
                new = list(tuple_interaction)
                with_powder = list(tuple_key)

                new[2] = self.prob_eval(new[2], types[with_powder[0]])
                if tuple_key in types and self.density < types[with_powder[0]].density: continue
                if new[0] == Keywords.current: new[0] = self.index
                if new[0] == Keywords.evaporate: new[0] = types[with_powder[0]].evaporates_into
                if new[1] == Keywords.current: new[1] = self.index

                if with_powder[0] == self.index: continue
                if not with_powder[3]:
                    with_powder[3] = []#self.fall_offsets.copy()
                    for offset in self.fall_offsets:
                        if not (offset[:2] in self.checks_set and not self.override_fall_offsets):
                            with_powder[3].append(offset[:2])
                    if not with_powder[3]: continue
                    with_powder[3] = tuple(with_powder[3])
                    new[3] = frozenset(with_powder[3])
                #if offset in self.interaction_checks: continue
                #del tuples[tuple_key]
                tuples[tuple(with_powder)] = tuple(new)

            self.interact_with_types |= tuples

        for interaction in self.add_interactions.values():
            self.interact_with_types |= interaction.to_tuples()

        # if self.index == 9:
        #     for inter in self.interact_with_types:
        #         if inter[0] == 2:
        #             print(inter)

        self.id_space = set([self.index << 8 | i for i in self.use_bits])

        offset_interactions = {}
        for with_type, interaction in self.interact_with_types.items():
            other_types = [with_type[0]] if with_type[0] is not None else Powder.all_elements
            other_bit_states = None
            is_custom_bit = False
            if with_type[1] is None:
                other_bit_states = types[with_type[0]].use_bits.copy()
            else:
                is_custom_bit = True
                other_bit_states = [with_type[1]] if isinstance(with_type[1], int) else with_type[1]
            iter_over = interaction[7] if not interaction[7][0] is None else self.use_bits
            if interaction[7][0] is not None:
                self.uses_bit_conds = True
            if_bit = set([self.index << 8 | i for i in iter_over])

            for other_type in other_types:
               # if other_type == self.index and not is_custom_bit: continue
                for other_bit in other_bit_states:
                    result_bit = other_type << 8 | other_bit

                    set_itself = interaction[0] if interaction[0] is not None else self.index

                    set_other = interaction[1] if interaction[1] is not None else other_type
                    set_itself_bit = interaction[4] if interaction[4] is not None else 0
                    set_other_bit = interaction[5] if interaction[5] is not None else 0
                    in_offsets = interaction[3] if interaction[3] else self.fall_offsets

                    bit_change_first = None
                    first_bit_changed = False
                    if interaction[8] is not None:
                        if interaction[8].relative_to_itself:
                            self.uses_bit_change = True
                            first_bit_changed = True
                            bit_change_first = interaction[8].value
                        else:
                            bit_change_first = other_type << 8 | other_bit + interaction[8].value

                    bit_change_second = None
                    second_bit_changed = False
                    if interaction[9] is not None:
                        if interaction[9].relative_to_itself:
                            self.uses_bit_change = True
                            second_bit_changed = True
                            bit_change_second = interaction[9].value
                        else:
                            bit_change_second = other_type << 8 | other_bit + interaction[9].value

                    if interaction[11]:
                        self.priority_types.add(result_bit)
                    val = [
                    set_itself << 8 | set_itself_bit if bit_change_first is None else bit_change_first,
                    set_other << 8 | set_other_bit if bit_change_second is None else bit_change_second,
                    interaction[2],
                    if_bit,
                    first_bit_changed,
                    second_bit_changed,
                    interaction[10],
                    interaction[11],
                    interaction[12]
                    ]
                    if interaction[10]:
                        self.has_expand = True
                    if interaction[12] != 1:
                        self.has_tick_modulus = True
                    if interaction[11]:
                        self.has_prioritized = True
                    #if  (0,0) in in_offsets:
                     #   print((result_bit, tuple(in_offsets), tuple(with_type[4])))
                    offset_interactions[(result_bit, tuple(in_offsets), tuple(with_type[4]))] = tuple(val)
                    #change_itself_bit,
                    #change_other_bit)
                    #if self.index == 10:
                    #    print(offset_interactions[(other_type << 8 | other_bit, tuple(in_offsets))][4])

                   # if interaction[8] is not None:
                   #     print(offset_interactions[(other_type << 8 | other_bit, tuple(in_offsets))][4])


        self.bit_interactions = {}

        for key, tuple_interaction in offset_interactions.items():
            bits = self.use_bits if key[2][0] is None else key[2]
            for bit in bits:
                new_bit = self.index << 8 | bit
                if not new_bit in self.bit_interactions:
                    self.bit_interactions[new_bit] = {}
                for offset in key[1]:
                    new_offset = (offset[0], offset[1])

                    if not new_offset in self.bit_interactions[new_bit]:
                        self.bit_interactions[new_bit][new_offset] = {}
                    self.bit_interactions[new_bit][new_offset][key[0]] = tuple_interaction

                for offset in self.fall_offsets:
                    if not offset[:2] in self.bit_interactions[new_bit]:
                        self.bit_interactions[new_bit][offset[:2]] = {}
                # if self.index == 10 and bit == 1:
                #     print(tuple_interaction)

        default = {offset: {} for offset in self.fall_offsets}
        for i in self.use_bits:
            bit_id = self.index << 8 | i
            if not bit_id in self.bit_interactions:
                logging.warning(f"No bit state found for SubPowder of {self.index}, with bit {i}")
                self.bit_interactions[bit_id] = default
            powder = SubPowder(self.bit_interactions[bit_id], self.id_space)
            powder.priority_types = self.priority_types
            if isinstance(self, Plant):
                powder.detatch_if = self.detatch_if
            update_types[bit_id] = powder


    def bind_interactions(self):
        for interaction in list(self.add_interactions.values()):
            #print(interaction.to_tuples())
            if interaction.double_sided and not interaction.is_with_bit:
                for with_powder, interaction_tuple in interaction.to_tuples().items():
                    if not with_powder[0] in types: continue
                    other_powder = types[with_powder[0]]
                    if not self.index in other_powder.add_interactions:
                        other_powder.add_interactions[(self.index, ())] = Interaction(self.index, interaction_tuple[1],
                                                                                      interaction_tuple[0],
                                                                                      interaction_tuple[2],
                                                                                      itself_bit_state=interaction_tuple[5],
                                                                                      other_bit_state=interaction_tuple[
                                                                                          4])
        for interaction in list(self.to_add_interactions):
            if interaction.double_sided and not interaction.is_with_bit:
                for with_powder, interaction_tuple in interaction.to_tuples().items():
                    if not with_powder[0] in types: continue
                    other_powder = types[with_powder[0]]
                    if 1:#not self.index in other_powder.add_interactions:
                        other_powder.to_add_interactions.append(Interaction(self.index, interaction_tuple[1] if interaction_tuple[1] != Keywords.current else self.index,
                                                                                      interaction_tuple[0] if interaction_tuple[0] != Keywords.current else self.index,
                                                                                      self.prob_eval(interaction_tuple[2], other_powder),
                                                                                      itself_bit_state=interaction_tuple[5],
                                                                                      other_bit_state=interaction_tuple[4],
                                                                                      ))


    def __init__(self, index: int,
                 class_tags: list = [PowderTags.Default],
                 throw_dice: bool = False,
                 gravity_direction: int = -1,
                 fall_direction: int = -1,
                 move_probability: int = 50,
                 override_fall_offsets: bool = False,
                 custom_interactions: list[Interaction] = [],
                 custom_scipt = "",
                 custom_cond = "",
                 use_bits = [0],
                 evaporates_into = 0,
                 add_interaction_checks = None,
                 add_fall_offsets = [],

                 density: int = 100,
                 flammability: int = 0,
                 temperature: int = 0,
                 meltability: int = 0,

                 turns_into: tuple[int, int, int] = None #into, probability, if bit state is..
                 ):
        self.to_add_interactions: list[Interaction] = []
        #print(self.__class__)
        self.class_tags = class_tags


        self.has_expand = False
        self.has_tick_modulus = False
        self.raw_interactions = {}
        self.evaporates_into = evaporates_into
        self.priority_types = set([])
        self.interact_with_types = {}
        self.is_plant = False
        self.has_bitwise_operations = False
        self.uses_bit_change = False
        self.uses_bit_conds = False
        self.has_prioritized = False
        #print(no_interactions_with)
        self.custom_script, self.custom_cond = custom_scipt, custom_cond
        self.gravity_direction = gravity_direction
        self.class_tags = list(class_tags)
        self.throw_dice = throw_dice
        self.index = index
        self.use_bits = use_bits

        self.density = density
        self.temperature = temperature
        self.meltability = meltability
        self.flammability = flammability

        if add_interaction_checks is None: add_interaction_checks = []
        #if turns_into is not None:
        #    add_interaction_checks.append((0, 0, turns_into[1], turns_into[2] if len(turns_into) > 2 else use_bits))


        for i in range(len(add_interaction_checks)):
            new = list(add_interaction_checks[i])
            if len(new) > 3:
                new[3] = frozenset(new[3])
            else:
                new.append(frozenset(self.use_bits))
            #if new[1] == 1 and index == 9:
            #    print(new)
            add_interaction_checks[i] = tuple(new)

        self.interaction_checks = set(add_interaction_checks)
        self.checks_set = set([offset[:2] for offset in add_interaction_checks])
        add_fall_offsets = add_fall_offsets.copy()
        add_fall_offsets += add_interaction_checks

        default_offsets = []
        self.override_fall_offsets = override_fall_offsets
        if not override_fall_offsets:
            default_offsets = [(0,gravity_direction,100), (-1,fall_direction,move_probability), (1,fall_direction,move_probability)]
        offsets_dict = dict({offset[0:2]: offset for offset in default_offsets})
        offsets_dict |= dict({offset[0:2]: offset for offset in add_fall_offsets})
       # print(add_fall_offsets)

        self.fall_offsets = []
        for offset in offsets_dict.values():
            if offset[2] > 0:
                self.fall_offsets.append(offset)


        self.add_interactions = {}
        for interaction in custom_interactions:
            self.add_interactions |= {key: interaction for key, _tuple in interaction.to_tuples().items()}

        self.bit_by_offset = {}
        for offset in self.fall_offsets + add_interaction_checks:
            bits = self.use_bits if len(offset) < 4 else offset[3]
            if not offset[:2] in self.bit_by_offset:
                self.bit_by_offset[offset[:2]] = []
            self.bit_by_offset[offset[:2]] += [self.index << 8 | bit for bit in bits]
        for offset,bits in self.bit_by_offset.items():
            self.bit_by_offset[offset] = frozenset(bits)


        #if self.bit_by_offset:
        #    print(self.bit_by_offset)


class StablePowder(Powder):
    class_tag_interactions = Powder.class_tag_interactions
    def __init__(self, index: int, **kwargs):
        super().__init__(index=index, **kwargs)

plant_heights = {}
class Plant(Powder):
    class_tag_interactions = Powder.class_tag_interactions
    def __init__(self, index: int,
                 growth_direction: int = 1,
                 growth_probability: int = 20,
                 growth_suitable: list[int] = [],
                 branch_probability: int = 5,
                 detatch_if: int | list[int] = [0],
                 detatched_powder: int = None,
                 height: int = 10):
        if isinstance(detatch_if, int): detatch_if = list(detatch_if)
        self.detatch_if = set([element << 8 for element in detatch_if]) if not detatch_if is None else None
        self.has_detatch = detatched_powder is not None
        self.on_detatch = detatched_powder
        super().__init__(index,
                        class_tags=[PowderTags.Plant],
                        throw_dice=True,
                        gravity_direction=growth_direction,
                        fall_direction=growth_direction,
                        flammability=90,
                        add_fall_offsets=[(-1,growth_direction, branch_probability),
                                          (1, growth_direction, branch_probability),
                                          (0, growth_direction, growth_probability)
                                          ],
                        use_bits=list(range(0, height+1))
                        #custom_interactions=[Interaction(with_powder=Powder.gases, itself_turns_into=powder_counterpart, other_turns_into=other, bit_change=-1)]
                        )
        self.is_plant = True
        #plant_heights[index] = height
        self.height = height
        for gas in growth_suitable:
            self.add_interactions[gas] = Interaction(with_powder=gas, itself_turns_into=index, other_turns_into=index, probability=100,
                                                     change_other_bit=BitRelative(relative_to_itself=True, value=1))



class Flame(Powder):
    class_tag_interactions = Powder.class_tag_interactions
    def __init__(self, index: int,
                 dissolve_time: int,
                 shift_probability: int = 5,
                 dissolve_probability: int = 100,
                 spread_speed: int = 50,
                 dissolve_in = [0],
                 absorb_in = [],
                 absorb_probability = 50,
                 ):
        super().__init__(
                temperature=spread_speed,
                index = index,
                class_tags=[PowderTags.Fire],
                use_bits=list(range(dissolve_time+1)),
                custom_interactions=[Interaction(with_powder=dissolve_in, itself_turns_into=Keywords.other, other_turns_into=index, probability=shift_probability, itself_bit_state=0,
                                                if_bit_state_is=list(range(0,dissolve_time)),
                                                change_other_bit=BitRelative(relative_to_itself=True, value=1),
                                                expand=True),
                                     Interaction(with_powder=absorb_in, itself_turns_into=0,
                                                 other_turns_into=Keywords.other, probability=absorb_probability,
                                                 itself_bit_state=0,
                                                 if_bit_state_is=list(range(0, dissolve_time))),
                                    Interaction(with_powder=index, itself_bit_state=0, itself_turns_into=0,
                                                if_bit_state_is=dissolve_time,
                                                other_turns_into=0, other_bit_state=0, in_offsets=[(0,0)], probability=dissolve_probability),
                                    Interaction(with_powder=index, itself_turns_into=index,
                                                change_other_bit=BitRelative(relative_to_itself=True, value=1), expand=True,
                                                other_turns_into=index,
                                                if_bit_state_is=list(range(0,dissolve_time)),
                                                probability=60),

                                     ],
                add_fall_offsets=[(0,-1,100), (0,1,100), (1,0,100), (-1,0,100)],
                add_interaction_checks=[(0,0,100)],
                throw_dice=True,
                density=-200,

            #flammability=90,
                override_fall_offsets = True
                        #custom_interactions=[Interaction(with_powder=Powder.gases, itself_turns_into=powder_counterpart, other_turns_into=other, bit_change=-1)]
                        )



from dataclasses import dataclass, field
@dataclass(frozen=True)
class SeedOf:
    plant_type: int
    hatch_spread_probability: int = 100
    suit_probability: int = 100
    growth_probability: int = 100
    suitable_in: list[int] | int = field(default_factory=list)



class Seed(Powder):
    class_tag_interactions = Powder.class_tag_interactions
    def __init__(self,
                 index: int,
                 gravity_direction: int = -1,
                 hatch_check_probability: int = 20,
                 growth_suitable: int | list[int] = 0,
                 seed_of: list[SeedOf] = [],
                 **kwargs):
        interactions = []
        bits = [0]
        for of in seed_of:
            bits.append(bits[-1]+1)
            suitable = of.suitable_in if isinstance(of.suitable_in, list) else [of.suitable_in]
            new = [
            Interaction(itself_turns_into=index, other_turns_into=index, probability=of.growth_probability,
                in_offsets=[(0, gravity_direction)],
                itself_bit_state=Keywords.other, other_bit_state=Keywords.other, with_powder=index, with_bit=bits[-1],
                if_bit_state_is=0),
            Interaction(with_powder=suitable, itself_turns_into=None, other_turns_into=None,
                probability=of.suit_probability,
                in_offsets=[(0, gravity_direction)],
                itself_bit_state=bits[-1], other_bit_state=0, if_bit_state_is=0),
            Interaction(with_powder=growth_suitable, itself_turns_into=of.plant_type, other_turns_into=Keywords.other,
                        probability=of.hatch_spread_probability,
                        in_offsets=[(0, -gravity_direction)],
                        itself_bit_state=0, other_bit_state=0, if_bit_state_is=bits[-1]),
            ]
            interactions += new
        super().__init__(index=index, gravity_direction=gravity_direction, fall_direction=gravity_direction, custom_interactions=interactions,
                         add_interaction_checks=[(0, -gravity_direction, hatch_check_probability, bits[1:])], use_bits=bits,
                         **kwargs)




types = {
    99: StablePowder(99, density=900, class_tags=[]),
    0: StablePowder(0, density=-100),
}

element_types = {}

import modules.unrolled_builder as unrolled_builder
unrolled = None
clears = {}

#from time import perf_counter

colors = []
names = []

import numpy as np
def _ready() -> None:
    types.update(element_types)
    for i in ["all_elements", "gases", "fires", "liquids", "solids", "meltables", "flammables", "hot"]:
        setattr(Powder, i, getattr(sys.modules[__name__], i))
    Powder.initialize()

 #   t = perf_counter()
    build_classes()
  #  print(perf_counter() - t)
    #print((types[1].bit_interactions))
    #quit()
    global unrolled
    unrolled_builder.StablePowder = StablePowder
    unrolled_builder.chunk_manager = chunk_manager
    unrolled_builder.types = types
    unrolled_builder.update_types = update_types
    global element_calls
    del types[0]
    element_calls = unrolled_builder.import_unrolled()

    arr = np.array(colors)
    render.plane.set_shader_parameter("uPalette", 0, arr.nbytes, arr)
    ui.UI_MATCH = {}
    for i in obtainable:
        ui.UI_MATCH[i] =  [names[i], colors[i]]
   # print(ui.UI_MATCH)
    render.plane.flush()

