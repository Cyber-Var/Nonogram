import pygame
from pygame.locals import *
import sys


class ScoreBoard:

    pygame.init()

    surface = pygame.Surface((100, 100))
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)

    score = 0
    lives = 3

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        smallfont = pygame.font.SysFont('Corbel', 25)

        text1 = smallfont.render('Score: ', True, self.COLOR_BLACK)
        self.surface.blit(text1, (10, 25))
        value1 = smallfont.render(str(self.score), True, self.COLOR_GREEN)
        self.surface.blit(value1, (65, 25))

        text2 = smallfont.render('Lives: ', True, self.COLOR_BLACK)
        self.surface.blit(text2, (10, 53))
        value2 = smallfont.render(str(self.lives), True, self.COLOR_RED)
        self.surface.blit(value2, (65, 53))

    def get_surface(self):
        return self.surface

    def correct(self):
        self.score += 10

    def incorrect(self):
        self.score -= 10
        self.lives -= 1


score = ScoreBoard(5)
