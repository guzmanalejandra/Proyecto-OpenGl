vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;
out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 0)/10, 1.0)).xyz;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 0)/10, 1.0);

}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;
uniform vec3 pointLight;
uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * intensity;
}
'''

toonShader = '''
#version 460

#define PI 3.14159265358979

layout (location = 0) out vec4 fragColor;
uniform vec3 color;
uniform float iTime;
in vec2 fragCoord;
in vec3 ourColor;
void main()
{
    vec2 iResolution = vec2(10, 10);
    fragColor = 9./max((fragCoord-iResolution.xy*.5)*mat2(cos(iTime-log(length(fragCoord))+vec4(0,11,33,0)))+9.,.1).xyyy;
}
'''
