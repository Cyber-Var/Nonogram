import pygame
from pygame.locals import *
import sys

pygame.init()

color_dark = (100, 100, 100)
displaysurface = pygame.display.set_mode((700, 700))
displaysurface.fill((255, 255, 255))

color_light = (200, 200, 200)
smallfont = pygame.font.SysFont('Corbel', 16)
text = smallfont.render('LOAD', True, color_light)

pygame.draw.rect(displaysurface, color_dark, [590, 315, 80, 30])
displaysurface.blit(text, (600, 320))

mouse = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print("mouse")
            if 590 <= mouse[0] <= 670 and 315 <= mouse[1] <= 345:
                print("Button clicked!")



    pygame.display.update()
