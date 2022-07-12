import sys

import pygame
from pygame.locals import *

pygame.init()

color1 = pygame.Color(0, 0, 0)
color2 = pygame.Color(255, 255, 255)
color3 = pygame.Color(128, 128, 128)
colorRed = pygame.Color(255, 0, 0)
colorGreen = pygame.Color(0, 255, 0)
colorBlue = pygame.Color(0, 0, 255)


DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill(color2)
pygame.display.set_caption("Example")


pygame.draw.polygon(DISPLAYSURF, colorRed, [(100, 100), (200, 100), (200, 200), (100, 200)])
pygame.draw.line(DISPLAYSURF, colorGreen, (100, 50), (200, 50))
pygame.draw.lines(DISPLAYSURF, colorBlue, True, [(100, 100), (200, 100),
                                                 (200, 100), (200, 200),
                                                 (200, 200), (100, 200),
                                                 (100, 200), (100, 100)], 2)
pygame.draw.circle(DISPLAYSURF, color2, (150, 150), 20)
pygame.draw.ellipse(DISPLAYSURF, color3, pygame.Rect(100, 150, 100, 10))
pygame.draw.rect(DISPLAYSURF, color1, pygame.Rect(100, 250, 100, 30), 10)

FPS = pygame.time.Clock()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FPS.tick(60)
