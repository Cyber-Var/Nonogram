import pygame
from pygame.locals import *
import sys

from LevelsMap import Levels


class Difficulties:
    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/difficulties_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    smallfont = pygame.font.SysFont('Corbel', 25)
    text_play = smallfont.render('Easy', True, (200, 200, 200))
    text_instructions = smallfont.render('Medium', True, (200, 200, 200))
    text_exit = smallfont.render('Hard', True, (200, 200, 200))

    def __init__(self):
        self.loop()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def loop(self):

        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 200 <= mouse[1] <= 230:
                        Levels(6)
                    elif 225 <= mouse[0] <= 375 and 350 <= mouse[1] <= 380:
                        Levels(8)
                    elif 250 <= mouse[0] <= 350 and 500 <= mouse[1] <= 530:
                        Levels(10)

            self.surface.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 200, 100, 30])
            self.surface.blit(self.text_play, (280, 207))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 350, 100, 30])
            self.surface.blit(self.text_instructions, (265, 357))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 500, 100, 30])
            self.surface.blit(self.text_exit, (280, 507))

            pygame.display.update()