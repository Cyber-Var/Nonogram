import pygame
import sys
from pygame.locals import *

from Square import Square


class Field:

    pygame.display.init()

    surface = pygame.Surface((500, 500))
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)

    squares = [[], [], [], [], [], []]

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                '''opacity = 1
                if self.squares[i][j].is_filled():
                    opacity = 0'''
                pygame.draw.rect(self.surface, self.COLOR_BLACK, [j * wh, i * wh, wh, wh], 1)

    def get_surface(self):
        return self.surface

    def arr(self):
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                self.arr[i][j] = Square(i, j)

    def set_squares(self, arr):
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if arr[i][j] == 1:
                    self.squares[i].append(Square(i, j, 1))
                else:
                    self.squares[i].append(Square(i, j))


field = Field(5)
