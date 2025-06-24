#version 400 core

layout(location = 0) in vec2 aPos;
layout(location = 1) in vec4 aColor;

uniform mat4 uProj;
uniform float uPointSize;
uniform vec2 mousePos;
uniform highp float shapeSize = 5;
uniform uint mode = 1u;

out vec2 uPos;

void main() {
    gl_Position = uProj * vec4(aPos + vec2(0.333,0), 0.0, 1.0);
    uPos = aPos;
    gl_PointSize = uPointSize;
}
