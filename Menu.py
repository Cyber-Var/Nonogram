import pygame
from pygame.locals import *
import sys
from math import trunc
import os.path


COLOR_WHITE = (255, 255, 255)
COLOR_TEXT = (250, 250, 250)
COLOR_RECT = (100, 100, 100)
COLOR_BLACK = (0, 0, 0)


def write_data(data=""):
    data_arr = data.split(":")
    if len(data_arr) >= 2:
        read_file = open("data.txt", "r")
        read_file_lines = read_file.readlines()
        write_file = open("data1.txt", "w")

        for line in read_file_lines:
            line_arr = line.split(":")
            if line_arr[0] != data_arr[0] or line_arr[1] != data_arr[1]:
                write_file.write(line)

        read_file.close()
        os.remove("data.txt")
        write_file.close()
        os.rename("data1.txt", "data.txt")
    if len(data_arr) == 6:
        if data_arr[5] == "True\n":
            file = open("scores.txt", "a")
            file.write(data_arr[3] + ":" + data_arr[4] + "\n")
            file.close()
    else:
        file = open("data.txt", "a")
        file.write(data)
        file.close()


def exit_game():
    pygame.quit()
    sys.exit()


class Menu:

    pygame.init()
    surface = pygame.display.set_mode((605, 700))

    bg_image = pygame.image.load('resources/backgrounds/menu_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)

    text_play = small_font.render('Play', True, COLOR_TEXT)
    text_record = small_font.render('View Record', True, COLOR_TEXT)
    text_instructions = small_font.render('Instructions', True, COLOR_TEXT)
    text_add = small_font.render('Add Level', True, COLOR_TEXT)
    text_exit = small_font.render('Exit', True, COLOR_TEXT)

    text_entry = small_font.render("", True, COLOR_RECT)

    record = 0

    def __init__(self):
        self.insert = ""
        self.active = False
        self.count_record()
        self.loop()

    def count_record(self):
        if os.path.isfile("scores.txt"):
            file = open("scores.txt", "r")
            file_lines = file.readlines()
            for line in file_lines:
                line_arr = line.split(":")
                self.record += int(line_arr[0]) + 20 * int(line_arr[1])

    def loop(self):

        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 350 and 100 <= mouse[1] <= 130:
                        Difficulties()
                    elif 225 <= mouse[0] <= 375 and 200 <= mouse[1] <= 230:
                        self.text_record = self.small_font.render("Record: " + str(self.record), True, COLOR_TEXT)
                    elif 225 <= mouse[0] <= 375 and 300 <= mouse[1] <= 330:
                        Instructions()
                    elif 250 <= mouse[0] <= 350 and 400 <= mouse[1] <= 430:
                        self.active = True
                        self.text_add = self.small_font.render("Difficulty:", True, COLOR_TEXT)
                        pygame.draw.rect(self.surface, COLOR_RECT, [350, 400, 50, 30], 2)
                    elif 250 <= mouse[0] <= 350 and 500 <= mouse[1] <= 530:
                        exit_game()
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            if self.insert.isdigit():
                                if int(self.insert) <= 25:
                                    Add(self.insert)
                            self.insert = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.insert = self.insert[:-1]
                        else:
                            self.insert += event.unicode
                        self.text_entry = self.small_font.render(self.insert, True, COLOR_RECT)

            self.surface.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 100, 100, 30])
            self.surface.blit(self.text_play, (280, 107))
            pygame.draw.rect(self.surface, COLOR_RECT, [225, 200, 150, 30])
            self.surface.blit(self.text_record, (250, 207))
            pygame.draw.rect(self.surface, COLOR_RECT, [225, 300, 150, 30])
            self.surface.blit(self.text_instructions, (250, 307))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 400, 100, 30])
            self.surface.blit(self.text_add, (260, 407))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 500, 100, 30])
            self.surface.blit(self.text_exit, (280, 507))

            if self.active:
                self.surface.blit(self.text_entry, (355, 407))
                pygame.draw.rect(self.surface, COLOR_RECT, [350, 400, 50, 30], 2)

            pygame.display.update()


class Add:
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/add_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)

    text_back = small_font.render('Back', True, COLOR_TEXT)

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
                    if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                        Menu()

            self.surface.blit(self.bg_image, (0, 0))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 635, 100, 30])
            self.surface.blit(self.text_back, (280, 642))

            pygame.display.flip()


class Instructions:

    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/instructions_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    big_font = pygame.font.SysFont('Corbel', 125)

    text_back = small_font.render('Back', True, COLOR_TEXT)
    text_one = small_font.render('Numbers on the top show how many tiles should be filled', True, COLOR_TEXT)
    text_two = small_font.render('in a column. Numbers on the left show how many tiles have', True, COLOR_TEXT)
    text_three = small_font.render('to be filled in a row.', True, COLOR_TEXT)
    text_four = small_font.render('Use the                button', True, COLOR_TEXT)
    text_five = small_font.render('to switch between fill', True, COLOR_TEXT)
    text_six = small_font.render('and cross modes.', True, COLOR_TEXT)
    text_seven = small_font.render('to go back to the', True, COLOR_TEXT)
    text_eight = small_font.render('previous window.', True, COLOR_TEXT)
    text_nine = small_font.render('If all tiles are filled correctly, the result image will be shown', True, COLOR_TEXT)
    text_ten = small_font.render('If you lose all 3 lives, no image will be displayed', True, COLOR_TEXT)
    text_heading = big_font.render('Instructions', True, (0, 0, 0))

    image_field = pygame.image.load('resources/instructions/field.jpeg')
    image_field = pygame.transform.scale(image_field, (300, 300))
    image_fill = pygame.image.load('resources/instructions/fill.jpeg')
    image_fill = pygame.transform.scale(image_fill, (30, 30))
    image_cross = pygame.image.load('resources/instructions/cross.jpeg')
    image_cross = pygame.transform.scale(image_cross, (30, 30))
    image_back = pygame.image.load('resources/instructions/back.jpeg')
    image_back = pygame.transform.scale(image_back, (70, 20))

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
            self.surface.blit(self.text_heading, (50, 20))

            self.surface.blit(self.text_one, (50, 120))
            self.surface.blit(self.text_two, (50, 150))
            self.surface.blit(self.text_three, (50, 180))

            self.surface.blit(self.image_field, (50, 210))

            self.surface.blit(self.text_four, (365, 270))
            self.surface.blit(self.image_fill, (430, 265))
            self.surface.blit(self.image_cross, (470, 265))
            self.surface.blit(self.text_five, (365, 300))
            self.surface.blit(self.text_six, (365, 330))

            self.surface.blit(self.text_four, (365, 400))
            self.surface.blit(self.image_back, (430, 400))
            self.surface.blit(self.text_seven, (365, 430))
            self.surface.blit(self.text_eight, (365, 460))

            self.surface.blit(self.text_nine, (50, 540))
            self.surface.blit(self.text_ten, (50, 570))

            pygame.draw.rect(self.surface, (100, 100, 100), [250, 635, 100, 30])
            self.surface.blit(self.text_back, (280, 642))

            pygame.display.flip()


class Difficulties:

    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/difficulties_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)

    text_easy = small_font.render('Easy', True, COLOR_TEXT)
    text_medium = small_font.render('Medium', True, COLOR_TEXT)
    text_hard = small_font.render('Hard', True, COLOR_TEXT)
    text_back = small_font.render('Back', True, COLOR_TEXT)

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
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 200, 100, 30])
            self.surface.blit(self.text_easy, (280, 207))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 350, 100, 30])
            self.surface.blit(self.text_medium, (265, 357))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 500, 100, 30])
            self.surface.blit(self.text_hard, (280, 507))
            pygame.draw.rect(self.surface, COLOR_RECT, [250, 635, 100, 30])
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

    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/levels_map_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)

    text = small_font.render('Back', True, COLOR_TEXT)

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
            pygame.draw.rect(self.surface, COLOR_WHITE, [80, 50, 70, 90], 1)
            # rocks:
            pygame.draw.rect(self.surface, COLOR_WHITE, [530, 120, 50, 50], 1)
            # house:
            pygame.draw.rect(self.surface, COLOR_WHITE, [5, 300, 80, 115], 1)
            # tree:
            pygame.draw.rect(self.surface, COLOR_WHITE, [185, 200, 85, 110], 1)
            # crystal:
            pygame.draw.rect(self.surface, COLOR_WHITE, [440, 315, 55, 70], 1)
            # statue:
            pygame.draw.rect(self.surface, COLOR_WHITE, [230, 405, 60, 120], 1)
            # fisher
            pygame.draw.rect(self.surface, COLOR_WHITE, [525, 440, 80, 100], 1)
            # car:
            pygame.draw.rect(self.surface, COLOR_WHITE, [375, 590, 90, 75], 1)

            pygame.draw.rect(self.surface, COLOR_RECT, [150, 635, 100, 30])
            self.surface.blit(self.text, (180, 642))

            pygame.display.update()


class Game:

    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/backgrounds/game_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    small_font = pygame.font.SysFont('Corbel', 25)
    big_font = pygame.font.SysFont('Corbel', 125)

    text = small_font.render('Back', True, COLOR_TEXT)

    file_data = {}
    old_data = []

    def __init__(self, difficulty, arr, level):
        self.difficulty = difficulty
        self.level = level
        self.arr = arr

        file_line = ""
        if os.path.isfile("data.txt"):
            data = open("data.txt", "r")

            for line in data.readlines():
                line_arr = line.split(":")
                if int(line_arr[0]) == self.difficulty and int(line_arr[1]) == self.level:
                    file_line = line
                key = line_arr[0] + ":" + line_arr[1]
                value = line.split(key, 1)[1]
                value = value[1: len(value)]
                self.file_data[key] = value

            file = open("data.txt", "w")
            everything = ""
            for key in self.file_data:
                file.write(key + ":" + self.file_data[key])
                everything += self.file_data[key]
            file.close()

            data.close()

        self.old_data = file_line.split(":")

        if len(self.old_data) != 5:
            self.field = Field(self.difficulty, self.arr)
            self.horizontal = HorizontalNumbers(self.difficulty, self.arr)
            self.vertical = VerticalNumbers(self.difficulty, self.arr)
            self.score = ScoreBoard(self.difficulty)
        else:
            self.field = Field(self.difficulty, self.arr, self.old_data[2])
            self.horizontal = HorizontalNumbers(self.difficulty, self.arr)
            self.vertical = VerticalNumbers(self.difficulty, self.arr)
            self.score = ScoreBoard(self.difficulty, self.old_data[3], self.old_data[4])
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

            pygame.draw.rect(self.surface, COLOR_RECT, [250, 635, 100, 30])
            self.surface.blit(self.text, (280, 642))

            pygame.display.flip()

    def loop(self):
        clock = pygame.time.Clock()

        fill = True
        end = True
        won = False
        while end:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    write_data(self.get_data())
                    exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    if 150 <= mouse[0] <= 250 and 635 <= mouse[1] <= 665:
                        write_data(self.get_data())
                        Menu()
                    elif 100 <= mouse[0] <= 600 and 100 <= mouse[1] <= 600:
                        handle = self.field.handle_mouse(mouse, fill)
                        if handle == 1:
                            self.score.correct()
                        elif handle == -1:
                            if self.score.incorrect() == -1:
                                end = False
                        if self.compare_squares(self.field.get_squares()):
                            won = True
                            end = False
                    elif 400 <= mouse[0] <= 440 and 625 <= mouse[1] <= 665:
                        fill = not fill

            self.surface.blit(self.bg_image, (0, 0))
            self.surface.blit(self.score.get_surface(), (0, 0))
            self.surface.blit(self.vertical.get_surface(), (0, 100))
            self.surface.blit(self.horizontal.get_surface(), (100, 0))
            self.surface.blit(self.field.get_surface(), (100, 100))

            pygame.draw.rect(self.surface, COLOR_RECT, [150, 635, 100, 30])
            self.surface.blit(self.text, (180, 642))

            pygame.draw.rect(self.surface, COLOR_RECT, [400, 625, 40, 40], 0, 10)
            pygame.draw.rect(self.surface, COLOR_BLACK, [400, 625, 40, 40], 2, 10)
            if fill:
                pygame.draw.rect(self.surface, COLOR_BLACK, [410, 635, 20, 20])
            else:
                pygame.draw.line(self.surface, COLOR_BLACK, (410, 635), (430, 655), 3)
                pygame.draw.line(self.surface, COLOR_BLACK, (430, 635), (410, 655), 3)

            pygame.display.flip()
            clock.tick(60)

        data = self.get_data()
        data = data.rstrip(data[-1])
        write_data(data + ":" + str(won) + "\n")
        self.end(won)

    def get_data(self):
        data = self.field.get_data()
        result = str(self.difficulty) + ":" + str(self.level) + ":"
        for i in range(len(data)):
            r = ""
            for j in range(len(data[i])):
                r += str(data[i][j])
            result += r + " "
        result = result.rstrip(result[-1])
        result += ":" + str(self.score.get_score()) + ":" + str(self.score.get_lives()) + "\n"
        return result


class Field:

    surface = pygame.Surface((500, 500))

    COLOR_PINK = (251, 92, 125)

    def __init__(self, difficulty, arr, old_data=""):
        self.difficulty = difficulty

        self.squares = []
        self.rectangles = []
        for n in range(self.difficulty):
            self.squares.append([])
            self.rectangles.append([])
        self.arr = arr

        if old_data == "":
            for i in range(self.difficulty):
                o_d = ""
                for j in range(self.difficulty):
                    o_d += "0"
                old_data += o_d + " "
            old_data = old_data.rstrip(old_data[-1])

        self.data = []
        old_data_arr = old_data.split(" ")
        for i in range(len(old_data_arr)):
            data = []
            old_data_arr1 = [*old_data_arr[i]]
            for j in range(len(old_data_arr1)):
                data.append(int(old_data_arr1[j]))
            self.data.append(data)

        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(200)
        self.surface.fill(COLOR_WHITE)

    def draw(self):
        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                rect = pygame.Rect(j * wh, i * wh, wh, wh)
                pygame.draw.rect(self.surface, COLOR_BLACK, rect, 1)
                self.squares[i].append(Square(i, j))
                self.rectangles[i].append(rect)

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 1:
                    self.squares[i][j].fill()
                    pygame.draw.rect(self.surface, COLOR_BLACK, self.rectangles[i][j], 0)
                elif self.data[i][j] == 2:
                    self.squares[i][j].cross()
                    rect = self.rectangles[i][j]
                    left = rect.left
                    top = rect.top
                    pygame.draw.line(self.surface, self.COLOR_PINK, (left, top), (left + rect.width, top + rect.height),
                                     4)
                    pygame.draw.line(self.surface, self.COLOR_PINK, (left + rect.width, top), (left, top + rect.height),
                                     4)
                elif self.data[i][j] == 3:
                    self.squares[i][j].cross()
                    rect = self.rectangles[i][j]
                    left = rect.left
                    top = rect.top
                    pygame.draw.line(self.surface, COLOR_BLACK, (left, top), (left + rect.width, top + rect.height), 4)
                    pygame.draw.line(self.surface, COLOR_BLACK, (left + rect.width, top), (left, top + rect.height), 4)
                elif self.data[i][j] == 4:
                    self.squares[i][j].fill()
                    pygame.draw.rect(self.surface, self.COLOR_PINK, self.rectangles[i][j], 0)

    def get_surface(self):
        return self.surface

    def get_squares(self):
        return self.squares

    def get_data(self):
        return self.data

    def handle_mouse(self, mouse, fill):
        wh = 500 / self.difficulty

        i = trunc((mouse[1] - 100) / wh)
        j = trunc((mouse[0] - 100) / wh)

        if self.squares[i][j].is_filled() or self.squares[i][j].is_crossed():
            return 0
        if fill:
            # Correct fill (black square)
            if self.arr[i][j] == 1:
                self.data[i][j] = 1
                self.squares[i][j].fill()
                pygame.draw.rect(self.surface, COLOR_BLACK, self.rectangles[i][j], 0)
                return 1
            # Incorrect fill (pink cross)
            else:
                self.data[i][j] = 2
                self.squares[i][j].cross()
                rect = self.rectangles[i][j]
                left = rect.left
                top = rect.top
                pygame.draw.line(self.surface, self.COLOR_PINK, (left, top), (left + rect.width, top + rect.height), 4)
                pygame.draw.line(self.surface, self.COLOR_PINK, (left + rect.width, top), (left, top + rect.height), 4)
                return -1
        else:
            # Correct cross (black cross)
            if self.arr[i][j] != 1:
                self.data[i][j] = 3
                self.squares[i][j].cross()
                rect = self.rectangles[i][j]
                left = rect.left
                top = rect.top
                pygame.draw.line(self.surface, COLOR_BLACK, (left, top), (left + rect.width, top + rect.height), 4)
                pygame.draw.line(self.surface, COLOR_BLACK, (left + rect.width, top), (left, top + rect.height), 4)
                return 1
            # Incorrect cross (pink square)
            else:
                self.data[i][j] = 4
                self.squares[i][j].fill()
                pygame.draw.rect(self.surface, self.COLOR_PINK, self.rectangles[i][j], 0)
                return -1


class HorizontalNumbers:

    surface = pygame.Surface((500, 100))

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty

        self.cols = []
        for n in range(self.difficulty):
            self.cols.append([])
        self.arr = arr

        self.initialise()
        self.set_cols()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(COLOR_WHITE)

    def draw(self):
        numbers = 0
        for col in self.cols:
            if len(col) > numbers:
                numbers = len(col)
        font_size = int(100 / numbers) - 5
        if font_size > 45:
            font_size = 45
        font = pygame.font.SysFont('arial', font_size)

        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            pygame.draw.line(self.surface, COLOR_RECT, (i * wh, 0), (i * wh, 100), 1)

            text = []
            for num in self.cols[i]:
                text.append(str(num))
            leftover = (100 - font_size * numbers) / (numbers + 1)
            y = leftover
            for line in text:
                number = font.render(line, True, COLOR_BLACK)
                self.surface.blit(number, (i * wh + wh / 2 - font_size / 3, y))
                y += leftover + font_size

        pygame.draw.line(self.surface, COLOR_RECT, (499, 0), (499, 100), 1)

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

    surface = pygame.Surface((100, 500))

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty

        self.rows = []
        for n in range(self.difficulty):
            self.rows.append([])
        self.arr = arr

        self.initialise()
        self.set_rows()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(COLOR_WHITE)

    def draw(self):
        numbers = 0
        for row in self.rows:
            if len(row) > numbers:
                numbers = len(row)
        font_size = int(100 / numbers)
        if font_size > 50:
            font_size = 50
        font = pygame.font.SysFont('arial', font_size)

        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            pygame.draw.line(self.surface, COLOR_RECT, (0, i * wh), (100, i * wh), 1)

            text = " "
            for num in self.rows[i]:
                text += str(num) + " "
            numbers = font.render(text, True, COLOR_BLACK)
            self.surface.blit(numbers, (10, i*wh + wh/2 - 2 * self.difficulty))

        pygame.draw.line(self.surface, COLOR_RECT, (0, 499), (100, 499), 1)

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

    surface = pygame.Surface((100, 100))

    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)

    small_font = pygame.font.SysFont('Corbel', 25)

    def __init__(self, difficulty, old_score="0", old_lives="3"):
        self.difficulty = difficulty
        self.score = int(old_score)
        self.lives = int(old_lives)

        self.initialise()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(COLOR_WHITE)

    def draw(self):
        text1 = self.small_font.render('Score: ', True, COLOR_BLACK)
        self.surface.blit(text1, (10, 25))
        value1 = self.small_font.render(str(self.score), True, self.COLOR_GREEN)
        self.surface.blit(value1, (65, 25))

        text2 = self.small_font.render('Lives: ', True, COLOR_BLACK)
        self.surface.blit(text2, (10, 53))
        value2 = self.small_font.render(str(self.lives), True, self.COLOR_RED)
        self.surface.blit(value2, (65, 53))

    def get_surface(self):
        return self.surface

    def get_score(self):
        return self.score

    def get_lives(self):
        return self.lives

    def correct(self):
        self.score += 10
        self.surface.fill(COLOR_WHITE)
        self.draw()

    def incorrect(self):
        if self.score >= 10:
            self.score -= 10
        self.lives -= 1
        self.surface.fill(COLOR_WHITE)
        self.draw()
        return self.lives


class Square:

    def __init__(self, x, y, filled=0):
        self.filled = filled
        self.crossed = 0
        self.x = x
        self.y = y

    def is_filled(self):
        return self.filled

    def fill(self):
        self.filled = 1

    def is_crossed(self):
        return self.crossed

    def cross(self):
        self.crossed = 1


Menu()
