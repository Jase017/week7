import random

class Bot():
    def make_move(self, board):
        while True:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if board[x][y] is None:
                return x, y
