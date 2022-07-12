import logging
import pygame
import sys
from pygame.locals import *


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


class GameWindow:
    logging.basicConfig()
    logging.root.setLevel(logging.NOTSET)
    pygame.init()

    def __init__(self):
        info = pygame.display.Info()
        self.display = pygame.display.set_mode((700, 700))
        self.display.fill((255, 255, 255))
        pygame.display.set_caption("Nonogram")
        update()

    def get_display(self):
        return self.display
