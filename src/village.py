from game.tile import tile

import pygame
from pygame.locals import *

pygame.init()
width = 20
height = 14 
side = 20
screen = pygame.display.set_mode([width * side, height * side])

pos = 0
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

def draw(screen):
    for y in range(height):
        for x in range(width):    
            tiles[y*(width)+x].blit(screen,[side*x, side*y])
    pygame.display.flip()


def game(pos):
    sprite = tiles[pos%(height*width)].get_topsprite()
    tiles[pos%(height*width)].set_topsprite(None)
    pos += 1
    tiles[pos%(height*width)].set_topsprite(sprite)

    return pos


while (pygame.event.poll().type != KEYDOWN):
    draw(screen)
    pos = game(pos)
    clock.tick(40)
