import sys

PROJECT_CLASSNAMES = [
    "variant", "ui", "render", "element_storage", "chunk_manager", "example"
]
GLOBAL_VARS = [
    "CHUNK_SIZE", "PIXEL_SIZE", "WINDOW_WIDTH", "WINDOW_HEIGHT", "CHUNKS_RECT", "CHUNK_PIXEL_SIZE"
]



WINDOW_WIDTH, WINDOW_HEIGHT = 773, 740
CHUNK_PIXEL_SIZE = 5.0
PIXEL_SIZE = 5.0
CHUNK_SIZE = 12
size_inc = (3*5-PIXEL_SIZE/3,5*5-PIXEL_SIZE/3)

CHUNKS_RECT = (1,2,12,12)

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
   # global clock
   # clock = pygame.time.Clock()
    pygame.display.set_caption("gl_test")
    for classname in PROJECT_CLASSNAMES:
        module = importlib.import_module("assets."+classname)
        modules.append(module)
        modules_dict[classname] = module
        if not classname in sys.modules:
            sys.modules[classname] = module
        setattr(sys.modules["__main__"], classname, module)
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

mouse_scroll_y = 0
mouse_just_pressed = False
def input_poll():
    global screen_mouse_position, mouse_just_pressed
    global mouse_pressed, prev_pressed
    global SELECTED_TYPE, index, mouse_scroll_y

    #key = pygame.key.get_pressed()
    # if key[pygame.K_a]:
    #     render.ShaderPlane("shaders/vertex.glsl", "shaders/fragment.glsl")

    mouse_just_pressed = False
    mouse_scroll_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

        if event.type == pygame.VIDEORESIZE:
            global WINDOW_WIDTH, WINDOW_HEIGHT
            WINDOW_WIDTH, WINDOW_HEIGHT = event.size

        if event.type == pygame.MOUSEMOTION:
            screen_mouse_position = event.pos

        if event.type == pygame.MOUSEWHEEL:
            mouse_scroll_y = 1 if event.y > 0 else -1

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pressed = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_just_pressed = not mouse_pressed
            mouse_pressed = True




SELECTED_TYPE = 1
index: int = 1

prev_pressed: bool = False
def _process(delta:float) -> bool:
    input_poll()

    for object in to_process:
        if not object.__name__ == "render":
            setattr(object, "WINDOW_WIDTH", WINDOW_WIDTH)
            setattr(object, "WINDOW_HEIGHT", WINDOW_HEIGHT)
        object._process(delta)

    pygame.display.flip()
   # clock.tick(120)

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