from OpenGL.GL import *
import numpy as np

TAGS = ["--no-processing"]
USE_MODULES = ["render", "variant"]
render = None
WINDOW_WIDTH, WINDOW_HEIGHT = None, None

# two FBOs + two textures for ping-pong
fbo_scene = None
fbo_pingpong = None
scene_tex = None
pingpong_tex = None

quadVAO = None
quadVBO = None

blur_shader_v = None
blur_shader_h = None



def create_float_texture(width: int, height: int) -> int:
    tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA16F, width, height, 0,
                 GL_RGBA, GL_FLOAT, None)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, 0)
    return tex

def create_fbo_for_texture(tex: int) -> int:
    fbo = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, fbo)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
                           GL_TEXTURE_2D, tex, 0)
    assert glCheckFramebufferStatus(GL_FRAMEBUFFER) == GL_FRAMEBUFFER_COMPLETE
    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    return fbo

def setup_fullscreen_quad() -> tuple[int,int]:
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    verts = np.array([
        # x,    y,    u, v
        -1.0, -1.0,  0.0, 0.0,
         1.0, -1.0,  1.0, 0.0,
         1.0,  1.0,  1.0, 1.0,
        -1.0,  1.0,  0.0, 1.0,
    ], dtype=np.float32)
    glBufferData(GL_ARRAY_BUFFER, verts.nbytes, verts, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))

    glBindVertexArray(0)
    return vao, vbo

def create_blur_shader(fragment_path: str,
                       width: int, height: int,
                       strength: float = 5.0,
                       threshold: float = 0.0) -> "ShaderPlane":
    sp = render.ShaderPlane(
        "shaders/screen_vertex.glsl",
        fragment_path,
        generate_vao=False,
        get_uniforms=["sceneTex", "threshold", "strength", "vSize"],
        set_default_uniforms=False
    )

    sp.set_shader_parameter_type("sceneTex", "glUniform1i")
    sp.set_shader_parameter_type("threshold", "glUniform1f")
    sp.set_shader_parameter_type("strength",  "glUniform1f")
    sp.set_shader_parameter_type("vSize", "glUniform2i")

    sp.set_shader_parameter("sceneTex", 0)
    sp.set_shader_parameter("threshold", threshold)
    sp.set_shader_parameter("strength", strength)
    sp.set_shader_parameter("vSize", width, height)

    glUseProgram(sp.program_id)
    sp.set_uniforms()
    glUseProgram(0)

    return sp


def _ready() -> None:
    global scene_tex, pingpong_tex
    global fbo_scene, fbo_pingpong
    global quadVAO, quadVBO
    global blur_shader_v, blur_shader_h

    scene_tex = create_float_texture(WINDOW_WIDTH, WINDOW_HEIGHT)
    pingpong_tex = create_float_texture(WINDOW_WIDTH, WINDOW_HEIGHT)
    fbo_scene = create_fbo_for_texture(scene_tex)
    fbo_pingpong = create_fbo_for_texture(pingpong_tex)

    quadVAO, quadVBO = setup_fullscreen_quad()

    blur_shader_h = create_blur_shader("shaders/screen_fragment_h.glsl",
                                       WINDOW_WIDTH, WINDOW_HEIGHT)
    blur_shader_v = create_blur_shader("shaders/screen_fragment_v.glsl",
                                       WINDOW_WIDTH, WINDOW_HEIGHT)

def open_framebuffer() -> None:

    glBindFramebuffer(GL_FRAMEBUFFER, fbo_scene)
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

def close_framebuffer() -> None:

    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

def draw_framebuffer() -> None:


    #glBindFramebuffer(GL_FRAMEBUFFER, fbo_pingpong)
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(blur_shader_h.program_id)
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, scene_tex)
    glBindVertexArray(quadVAO)
    glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
    glBindVertexArray(0)
    glUseProgram(0)

    # glBindFramebuffer(GL_FRAMEBUFFER, 0)
    # glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    # glClear(GL_COLOR_BUFFER_BIT)
    #
    # glUseProgram(blur_shader_v.program_id)
    # glActiveTexture(GL_TEXTURE0)
    # glBindTexture(GL_TEXTURE_2D, pingpong_tex)
    # glBindVertexArray(quadVAO)
    # glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
    # glBindVertexArray(0)
    # glUseProgram(0)