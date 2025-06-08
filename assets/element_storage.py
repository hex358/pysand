TAGS = ["--no-processing"]
USE_MODULES = ["chunk_manager", "mainloop"]
modules_dict = {}
chunk_manager = None
mainloop = None
ELEMENT_LIST = ["sand", "water", "lava", "steam", "dirt"]

import importlib
import sys
import numpy as np

elements_dict = {}
element_calls = {}
elements = []

burnables: dict[int] = {4: 10}
solids: set[int] = {9,3,4}
soft: set[int] = {0,2,6}
skip: set[int] = {0,9,3,4}
gases: set[int] = {6}

def clear(c):
    for call in clears.values():
        call(c)

clears = {}
def _ready() -> None:
    for element_name in ELEMENT_LIST:
        element = importlib.import_module(f"elements.{element_name}")
        elements_dict[element_name] = element; elements.append(element)
        element.chunk_manager = chunk_manager
        element.get_cell = chunk_manager.get_cell
        element_calls[element.CELL_INDEX] = element.update
        element.element_storage = sys.modules[__name__]
        if hasattr(element, "clear"):
            clears[element] = element.clear