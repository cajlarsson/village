from game.tile import tile

import pygame
from pygame.locals import *

pygame.init()

# Screen properties
screen_width = 51
screen_height = 29 
side = 20
screen = pygame.display.set_mode([screen_width * side, screen_height * side])

# Game properties
game_width = 100
game_height = 100

pos = 35

# Initialize sprites
bild1 = pygame.image.load("../res/test-alien.png")
bild1 = pygame.Surface.convert_alpha(bild1)
bild2 = pygame.image.load("../res/grass.png")
bild2 = pygame.Surface.convert_alpha(bild2)

# Create world
tiles = []
for i in range(game_width*game_height):
    if i == pos:
        tiles.append(tile(bild2,bild1))
    else:
        tiles.append(tile(bild2))

clock = pygame.time.Clock()

def draw(screen,corners=((0,0),(screen_width,screen_height))):
    """ Draws the dirty tiles in the rectangle given by corners (upper left
    corner, bottom right corner)"""
    x1 = corners[0][0]
    y1 = corners[0][1]
    x2 = corners[1][0]
    y2 = corners[1][1]

    xscreen = 0
    yscreen = 0

    for y in range(y1,y2):
        for x in range(x1,x2):    
            tiles[y*(game_width)+x].blit(screen,[side*xscreen, side*yscreen])
            xscreen += 1
        xscreen = 0
        yscreen += 1

    pygame.display.flip()


while (pygame.event.poll().type != KEYDOWN):
    draw(screen)
    #draw(screen,((20,0), (40,4)))
    #print(clock.get_fps())
    clock.tick(4)
