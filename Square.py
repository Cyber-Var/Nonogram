

class Square:

    def __init__(self, x, y, filled=0):
        self.filled = filled
        self.x = x
        self.y = y

    def is_filled(self):
        return self.filled

    def fill(self):
        self.filled = 1
