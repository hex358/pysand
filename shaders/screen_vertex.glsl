#version 330 core
layout(location = 0) in highp vec2 aPos;
layout(location = 1) in highp vec2 aUV;
uniform highp ivec2 vSize;
out vec2 uv;
void main() {
    uv = aUV;
    gl_Position = vec4(aPos, 0.0, 1.0);
}
