
TAGS = []
USE_MODULES = ["mainloop"]
modules_dict = {}
mainloop = None

import math

class Vector2:
    __slots__ = ("x","y")
    def __init__(self, x, y, i = False):
        self.x = x if not i else int(x)
        self.y = y if not i else int(y)
    def distance_to(self, vec: "Vector2"):
        return math.sqrt((vec.x - self.x) ** 2 + (vec.y - self.y) ** 2)
    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

deferred_queue: list = []

import os
import sys
def read_asset(path: str):
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.abspath(os.getcwd())
    return open(os.path.join(base, path), "r").read()

def call_deferred(call: callable, *args, **kwargs):
    deferred_queue.append((call, args, kwargs))
def _ready() -> None:
    pass

def _process(delta) -> None:
    for i in deferred_queue:
        slot = deferred_queue.pop()
        slot[0](*slot[1], **slot[2])
    deferred_queue.clear()