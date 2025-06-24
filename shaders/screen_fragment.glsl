#version 330 core
in vec2 uv;
out vec4 FragColor;

uniform sampler2D sceneTex;
uniform float threshold;
uniform float strength;
uniform ivec2 vSize;

vec3 blendMix(vec3 bg, vec3 fg, float fgA) {
    return fg * fgA + bg * (1.0 - fgA);
}

const float[9] weights = float[](0.016216, 0.054054,  0.1216216, 0.1945946, 0.227027, 0.1945946, 0.1216216, 0.054054, 0.016216);

void main() {
    vec4 orig = texture(sceneTex, uv);
    vec2 invRes = 1.0 / vec2(vSize);

    vec4 sum = vec4(0.0);
    float o = 5 * strength * invRes.y;
    for (int i = 0; i < 9; i ++){
        float y = uv.y + strength*invRes.y*i;
        sum += texture(sceneTex, vec2(uv.x, y))*weights[i];
    }
    vec4 new = sum;
    FragColor = vec4(blendMix(orig.rgb, new.rgb, new.a), orig.a);
}
