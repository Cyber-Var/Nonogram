import pygame
from pygame.locals import *
import sys


'''class HorizontalNumbers:

    pygame.init()

    surface = pygame.Surface((500, 100))
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (100, 100, 100)
    COLOR_BLACK = (0, 0, 0)

    cols = []

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty
        for n in range(self.difficulty):
            self.cols.append([])
        self.arr = arr
        self.initialise()
        self.set_cols()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        font = pygame.font.SysFont('arial', 25)

        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            pygame.draw.line(self.surface, self.COLOR_GRAY, (i * wh, 0), (i * wh, 100), 1)

            text = []
            for num in self.cols[i]:
                text.append(str(num))
            y = 10
            for line in text:
                number = font.render(line, True, self.COLOR_BLACK)
                self.surface.blit(number, (i * wh + wh / 2 - 20, y))
                y += 30

        pygame.draw.line(self.surface, self.COLOR_GRAY, (499, 0), (499, 100), 1)

    def get_surface(self):
        return self.surface

    def set_cols(self):
        summ = 0
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if self.arr[j][i] == 1:
                    summ += 1
                if (summ != 0 and self.arr[j][i] == 0) or (self.arr[j][i] == 1 and j == self.difficulty - 1):
                    self.cols[i].append(summ)
                    summ = 0'''
