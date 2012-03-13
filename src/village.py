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

start_pos = 224 

# Initialize sprites
bild1 = pygame.image.load("../res/test-alien.png")
bild1 = pygame.Surface.convert_alpha(bild1)
bild2 = pygame.image.load("../res/grass.png")
bild2 = pygame.Surface.convert_alpha(bild2)

# Create world
tiles = []
for i in range(game_width*game_height):
    if i == start_pos:
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
    
    changed = False

    xscreen = 0
    yscreen = 0

    for y in range(y1,y2):
        for x in range(x1,x2):    
            changed = tiles[y*(game_width)+x].blit(screen,[side*xscreen, side*yscreen]) or changed
            xscreen += 1
        xscreen = 0
        yscreen += 1

    if changed:
        pygame.display.flip()


def draw_all(screen,corners=((0,0),(screen_width,screen_height))):
    """ Draws all tiles in the rectangle given by corners (upper left
    corner, bottom right corner) regardless if they're dirty or not, and sets
    all tiles to clean"""
    x1 = corners[0][0]
    y1 = corners[0][1]
    x2 = corners[1][0]
    y2 = corners[1][1]

    changed = False

    xscreen = 0
    yscreen = 0

    for y in range(y1,y2):
        for x in range(x1,x2):    
            changed = tiles[y*(game_width)+x].blit(screen,[side*xscreen, side*yscreen], True) or changed
            xscreen += 1
        xscreen = 0
        yscreen += 1

    if changed:
        pygame.display.flip()


def run():
    xpos = 0
    ypos = 0

    draw_all(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key ==
                                      K_ESCAPE):
                return

        keystate = pygame.key.get_pressed()
        if keystate[K_LEFT]:
            if xpos > 0:
                xpos -= 1
                draw_all(screen,((xpos,ypos),(xpos+screen_width,ypos+screen_height)))

        if keystate[K_RIGHT]:
            if xpos < (game_width - screen_width):
                xpos += 1
                draw_all(screen,((xpos,ypos),(xpos+screen_width,ypos+screen_height)))

        if keystate[K_UP]:
            if ypos > 0:
                ypos -= 1
                draw_all(screen,((xpos,ypos),(xpos+screen_width,ypos+screen_height)))

        if keystate[K_DOWN]:
            if ypos < (game_height - screen_height):
                ypos += 1
                draw_all(screen,((xpos,ypos),(xpos+screen_width,ypos+screen_height)))

        draw(screen,((xpos,ypos),(xpos+screen_width,ypos+screen_height)))
        print(clock.get_fps())
        clock.tick(100)


run()
