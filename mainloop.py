import sys

PROJECT_CLASSNAMES = [
    "variant", "render", "element_storage", "chunk_manager", "ui", "example"
]
GLOBAL_VARS = [
    "CHUNK_SIZE", "PIXEL_SIZE", "WINDOW_WIDTH", "WINDOW_HEIGHT", "CHUNKS_RECT"
]
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
PIXEL_SIZE = 5.0
CHUNK_SIZE = 16

CHUNKS_RECT = (1,1,9,7)

import pygame
from pygame.locals import *
from OpenGL.GL import *
from time import time
import os
import importlib

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
modules = []
modules_dict: dict[str] = {"mainloop": sys.modules["__main__"]}
_pixels = 0
to_process = []


def _ready() -> None:
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("gl_test")
    for classname in PROJECT_CLASSNAMES:
        module = importlib.import_module("assets."+classname)
        modules.append(module)
        modules_dict[classname] = module
    pygame.init()

    for object in modules:
        tags = getattr(object, "TAGS") if hasattr(object, "TAGS") else []

        for var in GLOBAL_VARS:
            if hasattr(object, var):
                setattr(object, var, globals()[var])

        if hasattr(object, "USE_MODULES"):
            for module in object.USE_MODULES:
                if module.startswith("*"):
                    module = module[1:len(module)]
                    for name in vars(modules_dict[module]):
                        if name.startswith("_"): continue
                        if name in object.__dict__: continue
                        object.__dict__[name] = getattr(modules_dict[module], name)
                if hasattr(object, "modules_dict"):
                    object.modules_dict[module] = modules_dict[module]
                if hasattr(object, module):
                    setattr(object, module, modules_dict[module])

        if not "--no-processing" in tags:
            to_process.append(object)

    for object in modules:
        object._ready()



SELECTED_TYPE = 1
select_types = [0, 1, 2, 3]
index: int = 1

prev_pressed: bool = False
def _process(delta:float) -> bool:
    global screen_mouse_position
    global mouse_just_pressed
    global mouse_pressed
    global prev_pressed
    global SELECTED_TYPE, index

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not prev_pressed:
        index += 1
        if index >= len(select_types): index = 0
        SELECTED_TYPE = select_types[index]
    prev_pressed = keys[pygame.K_a]

    mouse_just_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        if event.type == pygame.MOUSEMOTION:
            screen_mouse_position = event.pos
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pressed = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_just_pressed = not mouse_pressed
            mouse_pressed = True
    for object in to_process:
        object._process(delta)
    pygame.display.flip()
    return True

import math

screen_mouse_position: tuple[int, int] = (0, 0)
mouse_pressed: bool = False

ticks:int = 0
time_passed = 0.0
delta_time: float = 0.0

def main():
    running = True
    global time_passed; global _pixels; global ticks; global delta_time
    delta:float = 0.0
    prev:float = time()
    while running:
        now = time()
        delta = now-prev
        delta_time = delta
        prev = now
        ticks += 1
        time_passed += delta
        if not _process(delta):
            return




if __name__ == "__main__":
    _ready()
    main()