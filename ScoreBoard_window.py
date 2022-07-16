from Game import Game


class ScoreBoard(Game):

    score = 0
    lives = 10

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def correct(self):
        self.score += 10

    def incorrect(self):
        self.lives -= 1
