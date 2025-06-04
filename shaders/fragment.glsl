#version 330 core
flat in int vTileID;
in vec2 outPos;

const vec4 uPalette[4] = vec4[](
    vec4(0.0, 0.0, 0.0, 0.0),
    vec4(0.75, 0.69, 0.50, 1.0),
    vec4(0.0,  0.5,  1.0, 0.8),
    vec4(0.7,  0.7,  0.7, 1.0)
);

out vec4 FragColor;

float rand(vec2 co) {
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

void main() {
    int idx = clamp(vTileID, 0, 3);
    vec4 baseColor = uPalette[idx];
    float noise;
    vec2 mix_range = vec2(0.9, 1.1);
    switch (idx){
        case 0:
            break;
        case 1:
            noise = rand(floor(outPos / 5.0)*5.0);
            mix_range = vec2(0.9,1.1); break;
        case 2:
            noise = rand(floor((outPos*20+vec2(500.0)) / 5.0)*5.0);
            mix_range = vec2(1.0,1.15); break;
        case 3:
            noise = rand(floor((outPos*50-vec2(500.0)) / 5.0)*5.0);
            mix_range = vec2(0.8,1.0); break;
    }
    float brightness = mix(mix_range.x, mix_range.y, noise);
    FragColor = vec4(baseColor.rgb * brightness, baseColor.a);
}
