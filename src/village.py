from game.tile import tile

import pygame
from pygame.locals import *

pygame.init()
width = 30
height = 15 
side = 20
screen = pygame.display.set_mode([width * side, height * side])

pos = 80
bild1 = pygame.image.load("../res/test-alien.png")
bild1 = pygame.Surface.convert_alpha(bild1)

bild2 = pygame.image.load("../res/grass.png")
bild2 = pygame.Surface.convert_alpha(bild2)

tiles = []
for i in range(width*height):
    if i == pos:
        tiles.append(tile(bild2,bild1))
    else:
        tiles.append(tile(bild2))


clock = pygame.time.Clock()

while pygame.event.poll().type != KEYDOWN:
    for y in range(height):
        for x in range(width):    
            tiles[y*(width-1)+x].blit(screen,[side*x, side*y])

    pygame.display.flip()
    print(clock.get_fps())
    clock.tick(40)
