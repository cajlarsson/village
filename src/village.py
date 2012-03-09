import time

import pygame
from pygame.locals import *

pygame.init()
width = 55
height = 50
side = 20
screen = pygame.display.set_mode([width * side, height * side])

pos = 0
bild = pygame.image.load("../res/test-alien.png")
bild = pygame.Surface.convert_alpha(bild)

last = time.time()

clock = pygame.time.Clock()
while pygame.event.poll().type != KEYDOWN:
    for x in range(width ):
       for y in range(height):    
           screen.blit(bild,[side * x , side * y] )
    pygame.display.flip()
    clock.tick()
    print(clock.get_fps())
    time.sleep(0.02)



