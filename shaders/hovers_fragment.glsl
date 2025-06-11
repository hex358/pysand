#version 330 core

in vec2 uPos;
out vec4 FragColor;
uniform highp vec2 mousePos;
uniform highp float uPointSize;

void main() {
    vec2 snapped = floor((uPos+vec2(1.333,1.333)*uPointSize)/uPointSize)*uPointSize;
    vec2 mouse_snapped = floor(mousePos / uPointSize) * uPointSize;
    FragColor = vec4(1)*step(distance(snapped, mouse_snapped), 60);
}
