#version 330 core
in vec2 uv;
out vec4 FragColor;

uniform sampler2D sceneTex;
uniform float threshold;
uniform float strength;
uniform highp ivec2 vSize;

void main() {
    vec3 col = texture(sceneTex, uv).rgb;
    FragColor = vec4(col*3, 0.2);
}
