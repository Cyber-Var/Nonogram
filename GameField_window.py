import pygame
import sys
from pygame.locals import *

from Game import Game


class Field(Game):

    pygame.init()

    surface = pygame.display.set_mode((600, 600))
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.initialise()
        self.draw()
        self.loop()

    def initialise(self):
        self.surface.fill(self.COLOR_WHITE)
        self.surface.convert()
        print("i")

    def draw(self):
        x = 0
        y = 0
        wh = 600 / self.difficulty
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                pygame.draw.rect(self.surface, self.COLOR_WHITE, [x, y, wh, wh])
                x += wh
                y += wh

    def loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


field = Field(5)


