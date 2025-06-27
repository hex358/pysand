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
    vec2 invRes = 1.0 / vec2(vSize);

    vec4 sum = orig;
    float o = 4 * strength * invRes.x;
    for (int i = 0; i < 9; i ++){
        float x = uv.x + strength*invRes.x*i - o;
        vec4 curr = texture(sceneTex, vec2(x, uv.y));
        int tile = int(curr.a);
        highp float k = 0.0;
        highp vec4 glow_modulate = vec4(1.0);
        switch (tile){
            case 5:
                k = 0.11;
                glow_modulate = vec4(1.3, 0.8, 0.4, 1.0);
                break;
            case 11:
                k = 0.13;
                glow_modulate = vec4(0.8, 0.3, 0.3, 1.0);
                break;

        }

        sum += vec4(curr.rgb*k*6, 1.0)*weights[i]*glow_modulate;
    }
    FragColor = vec4(sum.rgb, int(orig.a));//vec4(blendMix(vec4(orig.rgb, 1.0), sum).rgb, orig.a);
}
