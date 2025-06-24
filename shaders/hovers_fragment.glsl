#version 330 core

in vec2 uPos;
out vec4 FragColor;
uniform highp vec2 mousePos;
uniform highp float uPointSize;
uniform highp float shapeSize = 5;

uniform highp uint mode = 1u; // 1 = circle, 2 = box, 3 = noise

uniform uint[144] noiseBits = uint[](
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
);


bool getMaskBit(int x, int y) {
    int mx = x % 12;
    int my = y % 12;
    int idx = my * 12 + mx;
    return noiseBits[idx] == 1u;
}

void main() {
    vec2 pos = uPos - vec2(-5.5*0.333,-5.5*0.333);
    vec2 snapped = floor((pos+vec2(1.333,1.333)*uPointSize)/uPointSize)*uPointSize;
    highp vec2 mouse_snapped = mousePos;//floor((mousePos+vec2(1.333,1.333)*uPointSize) / uPointSize) * uPointSize;
    switch (mode){
        case 1u:
            FragColor = vec4(1,1,1,0.3)*step(distance(snapped, mouse_snapped), shapeSize*uPointSize);
            break;
        case 2u:
            FragColor = vec4(1,1,1,0.2)*step(abs(snapped.x-mouse_snapped.x), shapeSize*uPointSize)*step(abs(snapped.y-mouse_snapped.y), shapeSize*uPointSize);
            break;
        case 3u:
            ivec2 world = ivec2(snapped / uPointSize) - ivec2(mouse_snapped / uPointSize) + ivec2(shapeSize);
            bool mask = getMaskBit(world.x, world.y);
            FragColor = vec4(1,1,1,0.3)*step(distance(snapped, mouse_snapped), shapeSize*uPointSize) * float(mask);
            break;
    }

}
