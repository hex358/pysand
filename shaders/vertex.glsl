#version 400 core
layout(location = 0) in vec2 aPos;
layout(location = 1) in int aTileID;

uniform mat4 uProj;
uniform float uPointSize;

flat out int vTileID;
out vec2 outPos;

void main() {
    gl_Position = uProj * vec4(aPos, 0.0, 1.0);
    gl_PointSize = uPointSize;
    vTileID = aTileID;
    outPos = aPos;
}
