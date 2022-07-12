import pygame
import sys
from pygame.locals import *

pygame.init()
displaysurface = pygame.display.set_mode((300, 300))

mySurface = pygame.Surface((50, 50))
# print(mySurface.get_size())
# print(mySurface.get_width())
# print(mySurface.get_height())
# mySurface.convert()
mySurface2 = pygame.Surface((100, 50))
# mySurface2.convert()
# mySurfaceCopy = pygame.Surface.copy(mySurface)

mySurface.fill((0, 255, 0))
mySurface2.fill((0, 255, 0))

displaysurface.blit(mySurface, (50, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.blit(mySurface, (50, 50))
    displaysurface.blit(mySurface2, (50, 150))
    # displaysurface.blit(mySurfaceCopy, (50, 150))

    pygame.display.update()
