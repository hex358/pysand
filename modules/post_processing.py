from OpenGL.GL import *
import numpy as np

TAGS = ["--no-processing"]
USE_MODULES = ["render", "variant"]
render = None
WINDOW_WIDTH, WINDOW_HEIGHT = None, None

bloom_shader_plane = None
fbo = None
quadVAO = None
quadVBO = None
scene_tex = None
def _ready() -> None:
    global fbo, quadVAO, bloom_shader_plane, quadVBO, scene_tex
    scene_tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, scene_tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA16F, WINDOW_WIDTH, WINDOW_HEIGHT, 0,
                 GL_RGBA, GL_FLOAT, None)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    fbo = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, fbo)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
                           GL_TEXTURE_2D, scene_tex, 0)

    assert glCheckFramebufferStatus(GL_FRAMEBUFFER) == GL_FRAMEBUFFER_COMPLETE
    glBindFramebuffer(GL_FRAMEBUFFER, 0)

    quadVAO = glGenVertexArrays(1)
    quadVBO = glGenBuffers(1)
    glBindVertexArray(quadVAO)
    glBindBuffer(GL_ARRAY_BUFFER, quadVBO)
    quad_vertices = np.array([
        # x,   y,       uv
        -1,   -1,      0, 0,
        1,    -1,      1, 0,
        1,     1,      1, 1,
        -1,    1,      0, 1,
    ], dtype=np.float32)
    glBufferData(GL_ARRAY_BUFFER, quad_vertices.nbytes,
                 quad_vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))
    glBindVertexArray(0)

    bloom_shader_plane = render.ShaderPlane("shaders/screen_vertex.glsl", "shaders/screen_fragment.glsl", generate_vao=False,
    get_uniforms=["sceneTex", "threshold", "strength", "vSize"], set_default_uniforms=False)#render.link_program(render.compile_shader(""))
    bloom_shader_plane.set_shader_parameter_type("sceneTex", "glUniform1i")
    bloom_shader_plane.set_shader_parameter_type("threshold", "glUniform1f")
    bloom_shader_plane.set_shader_parameter_type("strength", "glUniform1f")
    bloom_shader_plane.set_shader_parameter_type("vSize", "glUniform2i")

    bloom_shader_plane.set_shader_parameter("sceneTex", 0)
    bloom_shader_plane.set_shader_parameter("threshold", 0.0)
    bloom_shader_plane.set_shader_parameter("strength", 5.0)
    bloom_shader_plane.set_shader_parameter("vSize", WINDOW_WIDTH, WINDOW_HEIGHT)

    glUseProgram(bloom_shader_plane.program_id)
    bloom_shader_plane.set_uniforms()
    glUseProgram(0)
   # bloom_shader_plane.

def open_framebuffer() -> None:
    glBindFramebuffer(GL_FRAMEBUFFER, fbo)
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

def close_framebuffer() -> None:
    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    #glClear(GL_COLOR_BUFFER_BIT)

def draw_framebuffer() -> None:

    #glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(bloom_shader_plane.program_id)
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, scene_tex)

    glBindVertexArray(quadVAO)
    glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
    glBindVertexArray(0)
    glUseProgram(0)