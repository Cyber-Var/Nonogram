from math import trunc

import pygame
import time

from Square import Square


class Field:

    pygame.display.init()

    surface = pygame.Surface((500, 500))
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_PINK = (255, 204, 203)

    squares = [[], [], [], [], [], []]
    rectangles = [[], [], [], [], [], []]

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty
        self.arr = arr
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
                rect = pygame.Rect(j * wh, i * wh, wh, wh)
                pygame.draw.rect(self.surface, self.COLOR_BLACK, rect, 1)
                self.squares[i].append(Square(i, j))
                self.rectangles[i].append(rect)

    def get_surface(self):
        return self.surface

    def get_squares(self):
        return self.squares

    def handle_mouse(self, mouse):
        wh = 500 / self.difficulty
        i = trunc(mouse[1] / wh) - 1
        j = trunc(mouse[0] / wh) - 1

        if self.arr[i][j] == 1:
            self.squares[i][j].fill()
            pygame.draw.rect(self.surface, self.COLOR_BLACK, self.rectangles[i][j], 0)
            return True
        else:
            pygame.draw.rect(self.surface, self.COLOR_PINK, self.rectangles[i][j], 0)
            pygame.draw.rect(self.surface, self.COLOR_BLACK, self.rectangles[i][j], 1)
            return False
