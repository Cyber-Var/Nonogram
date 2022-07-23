import pygame
from pygame.locals import *
import sys
from math import trunc


def exit_game():
    pygame.quit()
    sys.exit()


class Menu:

    pygame.init()
    surface = pygame.display.set_mode((605, 700))

    bg_image = pygame.image.load('resources/backgrounds/menu_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    text_play = small_font.render('Play', True, (200, 200, 200))
    text_instructions = small_font.render('Instructions', True, (200, 200, 200))
    text_exit = small_font.render('Exit', True, (200, 200, 200))

    def __init__(self):
        self.loop()

    def loop(self):
        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 200 <= mouse[1] <= 230:
                        Difficulties()
                    elif 225 <= mouse[0] <= 375 and 350 <= mouse[1] <= 380:
                        Instructions()
                    elif 250 <= mouse[0] <= 350 and 500 <= mouse[1] <= 530:
                        print("exit")
                        exit_game()

            self.surface.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 200, 100, 30])
            self.surface.blit(self.text_play, (280, 207))
            pygame.draw.rect(self.surface, (100, 100, 100), [225, 350, 150, 30])
            self.surface.blit(self.text_instructions, (250, 357))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 500, 100, 30])
            self.surface.blit(self.text_exit, (280, 507))

            pygame.display.update()


class Instructions:

    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/instructions_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    text = small_font.render('Back', True, (200, 200, 200))

    big_font = pygame.font.SysFont('Corbel', 125)
    text_heading = big_font.render('Instructions', True, (0, 0, 0))

    def __init__(self):
        self.loop()

    def loop(self):

        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        Menu()

            self.surface.blit(self.bg_image, (0, 0))
            self.surface.blit(self.text_heading, (50, 70))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text, (280, 642))

            pygame.display.flip()


class Difficulties:
    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/difficulties_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    text_easy = small_font.render('Easy', True, (200, 200, 200))
    text_medium = small_font.render('Medium', True, (200, 200, 200))
    text_hard = small_font.render('Hard', True, (200, 200, 200))
    text_back = small_font.render('Back', True, (200, 200, 200))

    def __init__(self):
        self.loop()

    def loop(self):

        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        Menu()
                    elif 250 <= mouse[0] <= 350 and 200 <= mouse[1] <= 230:
                        Levels(6)
                    elif 225 <= mouse[0] <= 375 and 350 <= mouse[1] <= 380:
                        Levels(8)
                    elif 250 <= mouse[0] <= 350 and 500 <= mouse[1] <= 530:
                        Levels(10)

            self.surface.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 200, 100, 30])
            self.surface.blit(self.text_easy, (280, 207))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 350, 100, 30])
            self.surface.blit(self.text_medium, (265, 357))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 500, 100, 30])
            self.surface.blit(self.text_hard, (280, 507))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text_back, (280, 642))

            pygame.display.flip()


def get_array(difficulty, level):
    arr = []

    filename = "arrays/hard.txt"
    if difficulty == 6:
        filename = "arrays/easy.txt"
    elif difficulty == 8:
        filename = "arrays/medium.txt"

    file = open(filename, 'r')
    lines = file.readlines()
    line = lines[level]
    rows = line.split(" ")

    for i in range(len(rows)):
        row = []
        rows[i] = rows[i].replace("\n", "")
        for j in range(len(rows[i])):
            row.append(int(rows[i][j]))
        arr.append(row)

    return arr


class Levels:
    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/levels_map_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    text = small_font.render('Back', True, (200, 200, 200))

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.loop()

    def loop(self):
        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 150 <= mouse[0] <= 250 and 635 <= mouse[1] <= 665:
                        Difficulties()
                    elif 80 <= mouse[0] <= 150 and 50 <= mouse[1] <= 140:
                        # tunnel
                        Game(self.difficulty, get_array(self.difficulty, 0), 0)
                    elif 530 <= mouse[0] <= 580 and 120 <= mouse[1] <= 170:
                        # rocks
                        Game(self.difficulty, get_array(self.difficulty, 1), 1)
                    elif 5 <= mouse[0] <= 85 and 300 <= mouse[1] <= 415:
                        # house
                        Game(self.difficulty, get_array(self.difficulty, 2), 2)
                    elif 185 <= mouse[0] <= 270 and 200 <= mouse[1] <= 310:
                        # tree
                        Game(self.difficulty, get_array(self.difficulty, 3), 3)
                    elif 440 <= mouse[0] <= 495 and 315 <= mouse[1] <= 385:
                        # crystal
                        Game(self.difficulty, get_array(self.difficulty, 4), 4)
                    elif 230 <= mouse[0] <= 290 and 405 <= mouse[1] <= 525:
                        # statue
                        Game(self.difficulty, get_array(self.difficulty, 5), 5)
                    elif 525 <= mouse[0] <= 605 and 440 <= mouse[1] <= 540:
                        # fisher
                        Game(self.difficulty, get_array(self.difficulty, 6), 6)
                    elif 375 <= mouse[0] <= 465 and 590 <= mouse[1] <= 665:
                        # car
                        Game(self.difficulty, get_array(self.difficulty, 7), 7)

            self.surface.blit(self.bg_image, (0, 0))
            # tunnel:
            pygame.draw.rect(self.surface, (255, 255, 255), [80, 50, 70, 90], 1)
            # rocks:
            pygame.draw.rect(self.surface, (255, 255, 255), [530, 120, 50, 50], 1)
            # house:
            pygame.draw.rect(self.surface, (255, 255, 255), [5, 300, 80, 115], 1)
            # tree:
            pygame.draw.rect(self.surface, (255, 255, 255), [185, 200, 85, 110], 1)
            # crystal:
            pygame.draw.rect(self.surface, (255, 255, 255), [440, 315, 55, 70], 1)
            # statue:
            pygame.draw.rect(self.surface, (255, 255, 255), [230, 405, 60, 120], 1)
            # fisher
            pygame.draw.rect(self.surface, (255, 255, 255), [525, 440, 80, 100], 1)
            # car:
            pygame.draw.rect(self.surface, (255, 255, 255), [375, 590, 90, 75], 1)

            pygame.draw.rect(self.surface, (100, 100, 100), [150, 635, 100, 30])
            self.surface.blit(self.text, (180, 642))

            pygame.display.update()


class Game:

    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/game_background.jpeg')
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

        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        Menu()

            if won:
                txt = self.big_font.render('You Won !!!', True, (255, 0, 0))
                self.surface.blit(txt, (70, 15))
                image = pygame.image.load(image_name)
                image = pygame.transform.scale(image, (500, 500))
                self.surface.blit(image, (50, 100))
            else:
                txt = self.big_font.render('You Lost :(', True, (0, 0, 0))
                self.surface.blit(txt, (70, 300))

            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text, (280, 642))

            pygame.display.flip()

    def loop(self):
        clock = pygame.time.Clock()

        end = True
        won_lost = False
        while end:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        Menu()
                    elif 100 <= mouse[0] <= 600 and 100 <= mouse[1] <= 600:
                        handle = self.field.handle_mouse(mouse)
                        if handle:
                            self.score.correct()
                        else:
                            if self.score.incorrect() == -1:
                                end = False
                        if self.compare_squares(self.field.get_squares()):
                            won_lost = True
                            end = False

            self.surface.blit(self.bg_image, (0, 0))
            self.surface.blit(self.score.get_surface(), (0, 0))
            self.surface.blit(self.vertical.get_surface(), (0, 100))
            self.surface.blit(self.horizontal.get_surface(), (100, 0))
            self.surface.blit(self.field.get_surface(), (100, 100))
            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text, (280, 642))

            pygame.display.flip()
            clock.tick(60)

        self.end(won_lost)


class Field:

    pygame.display.init()

    surface = pygame.Surface((500, 500))
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_PINK = (251, 92, 125)

    squares = []
    rectangles = []

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty
        for n in range(self.difficulty):
            self.squares.append([])
            self.rectangles.append([])
        self.arr = arr
        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(200)
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            for j in range(self.difficulty):
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

        i = trunc((mouse[1] - 100) / wh)
        j = trunc((mouse[0] - 100) / wh)

        if self.arr[i][j] == 1:
            self.squares[i][j].fill()
            pygame.draw.rect(self.surface, self.COLOR_BLACK, self.rectangles[i][j], 0)
            return True
        else:
            rect = self.rectangles[i][j]
            left = rect.left
            top = rect.top
            pygame.draw.line(self.surface, self.COLOR_PINK, (left, top), (left + rect.width, top + rect.height), 4)
            pygame.draw.line(self.surface, self.COLOR_PINK, (left + rect.width, top), (left, top + rect.height), 4)
            return False


class HorizontalNumbers:

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
        sums = 0
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if self.arr[j][i] == 1:
                    sums += 1
                if (sums != 0 and self.arr[j][i] == 0) or (self.arr[j][i] == 1 and j == self.difficulty - 1):
                    self.cols[i].append(sums)
                    sums = 0


class VerticalNumbers:

    pygame.init()

    surface = pygame.Surface((100, 500))
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (100, 100, 100)
    COLOR_BLACK = (0, 0, 0)

    rows = []

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty
        for n in range(self.difficulty):
            self.rows.append([])
        self.arr = arr
        self.initialise()
        self.set_rows()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        font = pygame.font.SysFont('arial', 25)

        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            pygame.draw.line(self.surface, self.COLOR_GRAY, (0, i * wh), (100, i * wh), 1)

            text = " "
            for num in self.rows[i]:
                text += str(num) + " "
            numbers = font.render(text, True, self.COLOR_BLACK)
            self.surface.blit(numbers, (10, i*wh + wh/2 - 10))

        pygame.draw.line(self.surface, self.COLOR_GRAY, (0, 499), (100, 499), 1)

    def get_surface(self):
        return self.surface

    def set_rows(self):
        sums = 0
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if self.arr[i][j] == 1:
                    sums += 1
                if (sums != 0 and self.arr[i][j] == 0) or (self.arr[i][j] == 1 and j == self.difficulty - 1):
                    self.rows[i].append(sums)
                    sums = 0


class ScoreBoard:

    pygame.init()

    surface = pygame.Surface((100, 100))
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)
    small_font = pygame.font.SysFont('Corbel', 25)

    score = 0
    lives = 3

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        text1 = self.small_font.render('Score: ', True, self.COLOR_BLACK)
        self.surface.blit(text1, (10, 25))
        value1 = self.small_font.render(str(self.score), True, self.COLOR_GREEN)
        self.surface.blit(value1, (65, 25))

        text2 = self.small_font.render('Lives: ', True, self.COLOR_BLACK)
        self.surface.blit(text2, (10, 53))
        value2 = self.small_font.render(str(self.lives), True, self.COLOR_RED)
        self.surface.blit(value2, (65, 53))

    def get_surface(self):
        return self.surface

    def correct(self):
        self.score += 10
        self.surface.fill(self.COLOR_WHITE)
        self.draw()

    def incorrect(self):
        if self.score >= 10:
            self.score -= 10
        self.lives -= 1
        self.surface.fill(self.COLOR_WHITE)
        self.draw()
        return self.lives


class Square:

    def __init__(self, x, y, filled=0):
        self.filled = filled
        self.x = x
        self.y = y

    def is_filled(self):
        return self.filled

    def fill(self):
        self.filled = 1


Menu()
