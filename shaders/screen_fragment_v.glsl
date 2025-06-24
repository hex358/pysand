#version 400 core
in vec2 uv;
out vec4 FragColor;

uniform sampler2D sceneTex;
uniform float threshold;
uniform float strength;
uniform ivec2 vSize;

vec4 blendMix(vec4 bg, vec4 fg) {
    fg.r = clamp(fg.r, 0.0, 1.0);
    fg.g = clamp(fg.g, 0.0, 1.0);
    fg.b = clamp(fg.b, 0.0, 1.0);
    fg.a = clamp(fg.a , 0.0, 1.0);

    bg.r = clamp(bg.r, 0.0, 1.0);
    bg.g = clamp(bg.g, 0.0, 1.0);
    bg.b = clamp(bg.b , 0.0, 1.0);
    bg.a = clamp(bg.a , 0.0, 1.0);
    float outA = fg.a + bg.a * (1.0 - fg.a);
    vec3 outRGB = (fg.rgb * fg.a + bg.rgb * bg.a * (1.0 - fg.a))
                  / max(outA, 0.0001);
    return vec4(outRGB, outA);
}

const float[9] weights = float[](0.016216, 0.054054,  0.1216216, 0.1945946, 0.227027, 0.1945946, 0.1216216, 0.054054, 0.016216);

void main() {
    vec4 orig = texture(sceneTex, uv);
//    vec2 invRes = 1.0 / vec2(vSize);
//
//    vec4 sum = vec4(0.0);
//    float o = 4 * strength * invRes.y;
//    for (int i = 0; i < 9; i ++){
//        float y = uv.y + strength*invRes.y*i - o;
//        vec4 curr = texture(sceneTex, vec2(uv.x, y));
//        sum += vec4(curr.rgb, 1.0)*weights[i];
//    }
//    sum.a *= 0.8;
    FragColor = vec4(orig.r, orig.r, orig.r, 1.0);//vec4(orig.rgb, 1.0);
}
