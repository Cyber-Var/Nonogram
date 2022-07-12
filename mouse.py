import pygame
from pygame.locals import *
import sys

pygame.init()
display = pygame.display.set_mode((300, 300))
FPS_CLOCK = pygame.time.Clock()


class Player:
    def __init__(self):
        self.rect = pygame.draw.rect(display, (255, 0, 0), (100, 100, 100, 100))

player = Player()

while 1:
    flag = 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Player")
        if event.type == MOUSEBUTTONUP:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse released on the Player")
        if event.type == KEYDOWN:
            if event.key == K_a:
                if flag == 1:
                    pygame.mouse.set_visible(False)
                    flag = 0
                elif flag == 0:
                    pygame.mouse.set_visible(True)
                    flag = 1
            if event.key == K_1:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.key == K_2:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    '''left, middle, right = pygame.mouse.get_pressed()'''

    pygame.display.update()
    FPS_CLOCK.tick(30)

