#version 330 core
flat in int vTileID;
in vec2 outPos;

const vec4 uPalette[11] = vec4[](
    vec4(0.0, 0.0, 0.0, 0.0),
    vec4(0.75, 0.69, 0.50, 1.0),
    vec4(0.0,  0.5,  1.0, 0.8),
    vec4(0.7,  0.7,  0.7, 1.0),
    vec4(0.33,  0.24,  0.19, 1.0),
    vec4(0.9,  0.4,  0.2, 0.9),
    vec4(0.6,  0.6,  0.8, 0.5),
    vec4(0.33,  0.19,  0.19, 1.0),
    vec4(0.23,  0.09,  0.11, 1.0),
    vec4(0.6,  0.8,  0, 1.0),
    vec4(0,  1,  0, 1.0)
);

out vec4 FragColor;

float rand(vec2 co) {
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

void main() {
    int tile = vTileID >> 8;
    vec4 baseColor = uPalette[tile];
    //if ((vTileID & 0xFF) > 0) {baseColor = vec4((vTileID & 0xFF)/3.0,0,0,1);}
    float noise = 1.0;
    vec2 mix_range = vec2(1,1);

    if (tile != 6){
    noise = rand(floor(outPos / 5.0)*5.0);
    mix_range = vec2(0.9,1.1);}

    float brightness = mix(mix_range.x, mix_range.y, noise);
    FragColor = vec4(baseColor.rgb * brightness, baseColor.a);
}
