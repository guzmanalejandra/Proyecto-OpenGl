import pygame
from pygame.locals import *

from shaders import *
from pygame import mixer 

from gl import Renderer, Model

from pickle import TRUE
from math import cos, sin, radians

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Proyecto Final")

mixer.music.load("musica.mp3")
mixer.music.play(-1)

clock = pygame.time.Clock()

rend = Renderer(screen)


rend.setShaders(vertex_shader, fragment_shader, toonShader)

rend.target.z = -5

tele = Model("televieja.obj", "tele.bmp")

tele.position.z -= 5
tele.scale.x = 0.5
tele.scale.y = 0.5
tele.scale.z = 0.5

bugs = Model("BugsBunny.obj", "bunny.bmp")
bugs.position.z -= 5
bugs.scale.x = 2
bugs.scale.y = 2
bugs.scale.z = 2

porki = Model("porki.obj", "porki.bmp")
porki.position.z -= 5
porki.scale.x = 2
porki.scale.y = 2
porki.scale.z = 2


correcaminos = Model("road_runner.obj", "road_runner_1.bmp")
correcaminos.position.z -= 5
correcaminos.scale.x = 2
correcaminos.scale.y = 2
correcaminos.scale.z = 2


coyote = Model("wile.obj", "wilee.bmp")
coyote.position.z -= 5
coyote.scale.x = 0.20
coyote.scale.y = 0.20
coyote.scale.z = 0.20

ground = Model("Rectangle.obj", "black.bmp")
ground.position.z -= 0
ground.position.x -= -0.30
ground.scale.x = 10
ground.scale.y = 0
ground.scale.z = 10




# face.position.z -= 10

rend.scene.append( tele )
rend.scene.append(ground)


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            

    if keys[K_q]:
        if rend.camDistance > 2:
            rend.camDistance -= 2 * deltaTime
    elif keys[K_e]:
        if rend.camDistance < 10:
            rend.camDistance += 2 * deltaTime

    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime


    if keys[K_w]:
        if rend.camPosition.y < 2:
            rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        if rend.camPosition.y > -2:
            rend.camPosition.y -= 5 * deltaTime

    if keys[K_n]:
        rend.scene.clear()
        rend.scene.append( tele ),
        rend.scene.append(ground)
    elif keys[K_m]:
        rend.scene.clear()
        rend.scene.append( bugs),
        rend.scene.append(ground)
    elif keys[K_l]:
        rend.scene.clear()
        rend.scene.append( porki ),
        rend.scene.append(ground)
    elif keys[K_c]:
        rend.scene.clear()
        rend.scene.append( correcaminos ),
        rend.scene.append(ground)
    elif keys[K_v]:
        rend.scene.clear()
        rend.scene.append( coyote ),
        rend.scene.append(ground),

        

    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance

    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    deltaTime = clock.tick(60) / 1000
    #print(deltaTime)

    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()
    

    
def music():
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.update() 
    

    
pygame.quit()
