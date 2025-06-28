#version 400 core
flat in int vTileID;
in vec2 outPos;

precision highp float;
const highp vec3 bg_color = vec3(0.25);
const highp vec4 uPalette[13] = vec4[](
    vec4(0.2, 0.2, 0.2, 1.0),
    vec4(0.75, 0.69, 0.50, 1.0),
    vec4(0.0,  0.5,  1.0, 0.8),
    vec4(0.7,  0.7,  0.7, 1.0),
    vec4(0.33,  0.24,  0.19, 1.0),
    vec4(1,  0.45,  0.3, 0.9), //vec4(0.9,  0.3,  0.2, 0.9),
    vec4(0.6,  0.6,  0.8, 0.5),
    vec4(0.33,  0.19,  0.19, 1.0),
    vec4(0.23,  0.09,  0.11, 1.0),
    vec4(0.6,  0.8,  0, 1.0),
    vec4(0,  1,  0, 1.0),
    vec4(1,  0.5,  0, 1.0),
    vec4(0,  0.5,  0, 1.0)
);

out vec4 FragColor;

float rand(vec2 co) {
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

void main() {
    int tile = vTileID >> 8;
    vec4 baseColor = uPalette[tile];

    if (tile == 11) {
        float k = (vTileID & 0xFF)/9.0;
        baseColor.a *= clamp(1.0-k*2, 0, 1);
        baseColor.r *= clamp(k*6, 1, 10);
        baseColor.g *= clamp(1.0-k*2, 0, 1);
        baseColor.b *= clamp(1.0-k*4, 0, 1);

        //baseColor *= 1.5;
    }
    if (baseColor.a < 0.001) {tile = 0; baseColor = vec4(0.0);}

    if (tile != 0){

    float noise = 1.0;
    vec2 mix_range = vec2(1,1);

    if (tile != 6){
    noise = rand(floor(outPos / 5.0)*5.0);
    mix_range = vec2(0.9,1.1);}

    float brightness = mix(mix_range.x, mix_range.y, noise);

    baseColor.rgb = baseColor.rgb*baseColor.a + bg_color*(1.0-baseColor.a);

    FragColor = vec4(baseColor.rgb * brightness, float(tile));}
    else{FragColor = vec4(bg_color,1.0);}
}
