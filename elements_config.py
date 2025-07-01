# You can add your own elements here.
#
# Note that you have to insert your colors into shaders/fragment.glsl manually,
# as usage of uniforms affects the perfomance very negatively.
#
# And generally speaking, tweak the shaders! it helps to personalize
# the game to your taste.

import modules.element_storage as el
from modules.element_storage import *

el.colors = [
(0.2, 0.2, 0.2, 1.0),
(0.75, 0.69, 0.50, 1.0),
(0.0, 0.5, 1.0, 0.8),
(0.7, 0.7, 0.7, 1.0),
(0.33, 0.24, 0.19, 1.0),
(1, 0.45, 0.3, 0.9),
(0.6, 0.6, 0.8, 0.5),
(0.33, 0.19, 0.19, 1.0),
(0.23, 0.09, 0.11, 1.0),
(0.6, 0.8, 0, 1.0),
(0, 1, 0, 1.0),
(1, 0.5, 0, 1.0),
(0, 0.5, 0, 1.0),
(0.5, 0.5, 0.4, 1.0),
]

el.names = [
    "AIR",
    "SAND",
    "WATER",
    "STONE",
    "WOOD",
    "LAVA",
    "VAPOR",
    "DIRT",
    "WET\nDIRT",
    "SEEDS",
    "GRASS",
    "FIRE",
    "DISSOLVED\nGRASS",
    "CAST\nIRON"
]

el.obtainable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]


el.all_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 99]
el.gases = [0, 6]
el.fires = [11]
el.liquids = [2, 5]
el.solids = [1, 3, 4, 7, 8, 9, 99]
el.meltables = [2, 13]
el.flammables = [4, 9, 10, 12]
el.hot = [5, 11]




el.element_types = {
    1: Powder(index=1,
                gravity_direction=-1,
                fall_direction=-1,
                density=80,
                move_probability=50),

    2: Powder(index=2,
                evaporates_into=6,
                meltability=100,
                density=40,
                class_tags=[PowderTags.Liquid],
                fall_direction=0,
                custom_interactions=[#Interaction(with_powder=5, double_sided=True, itself_turns_into=6, other_turns_into=5),
                                     Interaction(with_powder=7, itself_turns_into=2, other_turns_into=8, probability=100, double_sided=True)]),
    3: StablePowder(3),

    4: StablePowder(4, flammability=40),

    5: Powder(index=5,
                density=70,
                temperature=100,
                class_tags=[PowderTags.Liquid, PowderTags.Hot],
                move_probability=30,
                custom_interactions=[#Interaction(with_powder=[4, 9], itself_turns_into=0, other_turns_into=5, probability=30, double_sided=True),
                                    Interaction(with_powder=10, itself_turns_into=0, other_turns_into=5, probability=70),
                                    Interaction(with_powder=8, itself_turns_into=5, other_turns_into=7, probability=4)],
                fall_direction=0),

    6: Powder(index=6,
                density=-100,
                use_bits=[0,1],
                class_tags=[PowderTags.Gas],
                move_probability=50,
                custom_interactions=[
                Interaction(if_bit_state_is=0, with_powder=99, itself_bit_state=1, probability=100, in_offsets=[(0,1)]),
                Interaction(with_powder=6, with_bit=1, itself_bit_state=1, probability=100, if_bit_state_is=0, other_bit_state=1, in_offsets=[(0,1)]),
                Interaction(with_powder=0, if_bit_state_is=1, itself_turns_into=2, other_turns_into=Keywords.other, probability=100, in_offsets=[(0,-1)])],
                fall_direction=0,
                add_interaction_checks=[(0,-1,0.06)],
                gravity_direction=1),

    7: Powder(index=7,
                gravity_direction=-1,
                fall_direction=-1,
                density=80,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=8, itself_turns_into=7, other_turns_into=7, probability=10)]),

    8: Powder(index=8,
                gravity_direction=-1,
                fall_direction=-1,
                density=120,
                move_probability=30,
                custom_interactions=[Interaction(with_powder=7, itself_turns_into=8, other_turns_into=8, probability=2)],
                ),

    9: Seed(index=9, density=100, temperature=0, flammability=50, hatch_check_probability=1,
            seed_of=[SeedOf(plant_type=10, suitable_in=[7,8])]
                ),

    10: Plant(index=10,
            growth_direction=1,
            branch_probability=15,
            growth_probability=30,
            growth_suitable=[0, 6, 2],
            height=10,
            detatch_if=[0, 6, 2, 5, 12],
            detatched_powder=12

                ),

    11: Flame(11, 5, 5, 100, spread_speed=60, dissolve_in=[0, 6], absorb_in=[1,2, 5]),

    12: Powder(index=12,
        gravity_direction=-1,
        fall_direction=-1,
        flammability=90,
        density=80,
        move_probability=50),

    13: StablePowder(index=13, meltability=20)
}