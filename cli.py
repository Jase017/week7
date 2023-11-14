# cli.py
import random

from logic import Board, Player, Bot


class Game:
    def __init__(self):
        symbols = ['X', 'O']
        random.shuffle(symbols)

        num_of_players = None
        while num_of_players not in ['1', '2']:
            num_of_players = input("Enter the number of players (1/2): ")

        if num_of_players == '1':
            self.player1 = Player(symbols[0])
            self.player2 = Bot(symbols[1])
        elif num_of_players == '2':
            self.player1 = Player(symbols[0])
            self.player2 = Player(symbols[1])

        self.board = Board()
        self.current_player = self.player1

    def play(self):
        while not self.board.get_winner() and not self.board.is_draw():
            self.board.print_board()
            print('Next turn: ', self.current_player.symbol)
            x, y = self.current_player.make_move(self.board.board)
            if x == 'q' and y == 'q':
                print("Game exited by the player.")
                break
            self.board.board[x][y] = self.current_player.symbol
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

        winner = self.board.get_winner()

        self.board.print_board()

        if winner:
            print(winner, ' Won')
        elif self.board.is_draw():
            print("It's a draw.")


if __name__ == '__main__':
    while True:
        game = Game()
        game.play()
        while True:
            play_again = input('Do you want to play again? (Y/N): ')
            if play_again.upper() == 'Y':
                break
            elif play_again.upper() == 'N':
                exit()
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

