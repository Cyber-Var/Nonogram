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


class Menu:

    logging.basicConfig()
    logging.root.setLevel(logging.NOTSET)
    logger = logging.getLogger("Menu.class")
    pygame.init()

    def __init__(self, display):
        self.logger.info("Menu scene created.")
        self.display = display
        self.draw_buttons()

    def draw_buttons(self):
        color_dark = (100, 100, 100)
        color_light = (200, 200, 200)
        small_font = pygame.font.SysFont('Corbel', 30)

        text1 = small_font.render('Play', True, color_light)
        pygame.draw.rect(self.display, color_dark, [300, 150, 100, 50])
        self.display.blit(text1, (330, 165))

        text2 = small_font.render('Instructions', True, color_light)
        pygame.draw.rect(self.display, color_dark, [285, 250, 130, 50])
        self.display.blit(text2, (290, 265))

        text3 = small_font.render('Scores', True, color_light)
        pygame.draw.rect(self.display, color_dark, [300, 350, 100, 50])
        self.display.blit(text3, (317, 365))
