import pygame
from pygame.locals import *
import sys
import time

from GameField_window import Field
from HorizontalNumbers_window import HorizontalNumbers
from ScoreBoard_window import ScoreBoard
from VerticalNumbers_window import VerticalNumbers


class Game:

    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/game_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    text = small_font.render('Back', True, (200, 200, 200))

    big_font = pygame.font.SysFont('Corbel', 125)

    def __init__(self, difficulty, arr, level):
        self.difficulty = difficulty
        self.level = level

        self.arr = arr

        self.field = Field(self.difficulty, self.arr)
        self.horizontal = HorizontalNumbers(self.difficulty, self.arr)
        self.vertical = VerticalNumbers(self.difficulty, self.arr)
        self.score = ScoreBoard(self.difficulty)

        self.loop()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def compare_squares(self, squares):
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if self.arr[i][j] != squares[i][j].is_filled():
                    return False
        return True

    def end(self, won):
        self.surface.blit(self.bg_image, (0, 0))

        image_name = 'resources/'
        if self.difficulty == 6:
            image_name += 'easy'
        elif self.difficulty == 8:
            image_name += 'medium'
        else:
            image_name += 'hard'
        image_name += '/' + str(self.level) + '.jpeg'

        if won:
            txt = self.big_font.render('You Won !!!', True, (255, 0, 0))
            self.surface.blit(txt, (70, 15))
            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, (500, 500))
            self.surface.blit(image, (50, 100))
        else:
            txt = self.big_font.render('You Lost :(', True, (0, 0, 0))
            self.surface.blit(txt, (70, 300))

        pygame.display.update()
        time.sleep(2)
        self.exit_game()

    def loop(self):
        clock = pygame.time.Clock()

        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        self.exit_game()
                    elif 100 <= mouse[0] <= 600 and 100 <= mouse[1] <= 600:
                        handle = self.field.handle_mouse(mouse)
                        if handle:
                            self.score.correct()
                        else:
                            if self.score.incorrect() == -1:
                                self.end(False)
                        if self.compare_squares(self.field.get_squares()):
                            self.end(True)

            self.surface.blit(self.bg_image, (0, 0))
            self.surface.blit(self.score.get_surface(), (0, 0))
            self.surface.blit(self.vertical.get_surface(), (0, 100))
            self.surface.blit(self.horizontal.get_surface(), (100, 0))
            self.surface.blit(self.field.get_surface(), (100, 100))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text, (280, 642))

            pygame.display.flip()
            clock.tick(60)


'''easy = [[1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0]]


medium = [[0, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 0, 1, 1, 0, 0, 1, 1],
          [0, 0, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0]]

hard = [[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 1, 1, 0, 0, 0, 0, 1, 1, 0]]'''