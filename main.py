# ./main.py
# Mainloop. manages all the modules.
# On start, _ready function is called on every module.
# Then, every frame, it calls _process(delta) on them.

import sys
import config
import importlib
from time import time
from OpenGL.GL import *
from OpenGL.GLUT import *

PROJECT_CLASSNAMES = [
    "variant", "render", "element_storage", "ui", "post_processing", "chunk_manager", "example"
]
GLOBAL_VARS = [
    "CHUNK_SIZE", "PIXEL_SIZE", "WINDOW_WIDTH", "WINDOW_HEIGHT", "CHUNKS_RECT", "CHUNK_PIXEL_SIZE"
]

WINDOW_WIDTH, WINDOW_HEIGHT = 715, 680
CHUNK_PIXEL_SIZE = 5.0
PIXEL_SIZE = 5.0
CHUNK_SIZE = 12
size_inc = (3 * PIXEL_SIZE - 0, 3 * PIXEL_SIZE - 3 + PIXEL_SIZE)
CHUNKS_RECT = (1, 2, 11, 11)

to_process = []
to_before_process = []
modules = []
modules_dict = {"mainloop": sys.modules["__main__"]}

screen_mouse_position = (0, 0)
mouse_pressed = False
mouse_just_pressed = False
mouse_scroll_y = 0
just_space_pressed = False

SELECTED_TYPE = 1
index = 1

ticks = 0 #
time_passed = 0.0
delta_time = 0.0

prev_time = None

def _ready():
    for classname in PROJECT_CLASSNAMES:
        module = importlib.import_module("modules." + classname)
        modules.append(module)
        modules_dict[classname] = module
        if not classname in sys.modules:
            sys.modules[classname] = module
        setattr(sys.modules["__main__"], classname, module)

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
            if hasattr(object, "_before_process"):
                to_before_process.append(object)

    for object in modules:
        object._ready()


def display():
    global prev_time, delta_time, ticks, time_passed
    global mouse_just_pressed, mouse_scroll_y, just_space_pressed
    #print(mouse_scroll_y)
    now = time()
    if prev_time is None:
        prev_time = now
    delta = now - prev_time
    delta_time = delta
    prev_time = now
    time_passed += delta
    ticks += 1

    for module in to_before_process:
        module._before_process(delta)
    for module in to_process:
        module._process(delta)

    glutSwapBuffers()
    glutPostRedisplay()
    mouse_just_pressed = False
    mouse_scroll_y = 0
    just_space_pressed = False

def reshape(width, height):

    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH, WINDOW_HEIGHT = width, height
    # if (WINDOW_HEIGHT, WINDOW_WIDTH) == (HEIGHT, WIDTH):
    #     glViewport(0, 0, width, height)
    #     glMatrixMode(GL_PROJECTION)
    #     glLoadIdentity()
    #     glOrtho(0, width, 0, height, -1.0, 1.0)
    #     glMatrixMode(GL_MODELVIEW)




def keyboard(key, x, y):
    global just_space_pressed
    if key == b' ':
        if not just_space_pressed:
            ui.buttons['pause_button'].press()
        just_space_pressed = True
    elif key == b'\x1b':
       quit()


def mouse(button, state, x, y):
    global mouse_pressed, mouse_just_pressed, mouse_scroll_y, screen_mouse_position
    screen_mouse_position = (x, y)
    #print(button == GLUT_LEFT_BUTTON AND )
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_just_pressed = not mouse_pressed
            mouse_pressed = True
        elif state == GLUT_UP:
            mouse_pressed = False

    if state == GLUT_DOWN and button == 3:
        mouse_scroll_y = 1
    elif state == GLUT_DOWN and button == 4:
        mouse_scroll_y = -1


def motion(x, y):
    global screen_mouse_position
    screen_mouse_position = (x, y)


def passive_motion(x, y):
    global screen_mouse_position
    screen_mouse_position = (x, y)


def idle():
    glutPostRedisplay()



def main():
    print("AAAAA")
    glutInit(sys.argv)

    print("GL version:", (GL_VERSION))
   # glutInitContextVersion(4, 3)
    #glutInitContextProfile(GLUT_CORE_PROFILE)
    glutInitWindowPosition(glutGet(GLUT_SCREEN_WIDTH)//2-WINDOW_WIDTH//2, glutGet(GLUT_SCREEN_HEIGHT)//2-WINDOW_HEIGHT//2)
    #glutInitWindowPosition()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    glutCreateWindow(b"PySand")


    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutPassiveMotionFunc(passive_motion)


    glutIdleFunc(idle)

    _ready()
    glutMainLoop()

if __name__ == "__main__":
    main()
