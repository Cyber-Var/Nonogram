import pygame
from pygame.locals import *
import sys


class Instructions:

    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/instructions_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    text = small_font.render('Back', True, (200, 200, 200))

    big_font = pygame.font.SysFont('Corbel', 125)
    text_heading = big_font.render('Instructions', True, (0, 0, 0))

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
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        self.exit_game()

            self.surface.blit(self.bg_image, (0, 0))
            self.surface.blit(self.text_heading, (50, 70))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text, (280, 642))

            pygame.display.update()
