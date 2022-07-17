import pygame
from pygame.locals import *
import sys


class HorizontalNumbers:

    pygame.init()

    surface = pygame.Surface((500, 100))
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (100, 100, 100)

    def __init__(self, difficulty, list):
        self.difficulty = difficulty
        self.list = list
        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            pygame.draw.line(self.surface, self.COLOR_GRAY, (i * wh, 0), (i * wh, 100), 1)
        pygame.draw.line(self.surface, self.COLOR_GRAY, (499, 0), (499, 100), 1)

    def get_surface(self):
        return self.surface


numbers = HorizontalNumbers(5, [])
