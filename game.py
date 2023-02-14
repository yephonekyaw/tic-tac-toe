import math, random
import time
from player import *


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    @staticmethod
    def print_nums_board():
        # To display when the game is started
        # so that players will be noticed
        # how to choose the spot in their turns
        nums_board = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for row in nums_board:
            print('| ' + ' | '.join(row) + ' |')

    def print_board(self):
        for row in [self.board[i*3: (i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # Replace an empty spot with player's avatar
    def make_spot_owned(self, spot, avatar):
        if self.board[spot] == ' ':
            self.board[spot] = avatar
            if self.check_winner(spot, avatar):
                self.winner = avatar
            return True
        return False

    def check_winner(self, spot, avatar):
        row_ind = math.floor(spot / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([val == avatar for val in row]):
            return True
        
        col_ind = spot % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([val == avatar for val in col]):
            return True
        
        if spot % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([val == avatar for val in diagonal_1]):
                return True
            
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([val == avatar for val in diagonal_2]):
                return True
        return False

    def available_spots(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def empty_spots(self):
        return ' ' in self.board

    def num_empty_spots(self):
        return self.board.count(' ')


def game_intro():
    print("\nWelcome to Tic Tac Toe!")
    print("\nAvailable modes!!!")
    print("1. Human Vs Human")
    print("2. Human Vs Computer (Easy)")
    print("3. Human Vs Computer (Impossible)\n")

def choose_mode():
    mode = input("Please select the mode(1-3)! : ")    
    while True:
        try:
            mode = int(mode)
            if not 1 <= mode <= 3:
                raise ValueError
            return mode
        except ValueError:
            mode = input("\nInvalid Input! Enter again(1-3)! : ")

def create_player(mode):
    avatar_1 = input("\nChoose player one's avatar (X or O) : ")
    avatar_2 = 'X' if avatar_1 == 'O' else 'O'
    print(f'\nPlayer one \"{avatar_1}\" and Player two \"{avatar_2}\"\n')

    if mode == 1:
        player_1 = HumanPlayer(avatar_1)
        player_2 = HumanPlayer(avatar_2)
    elif mode == 2:
        player_1 = HumanPlayer(avatar_1)
        player_2 = ComputerPlayerEsay(avatar_2)
    elif mode == 3:
        player_1 = HumanPlayer(avatar_1)
        player_2 = ComptuerPlayerImpossible(avatar_2)
    return player_1, player_2

def play_game(tic_tac_toe, player_1, player_2):
    tic_tac_toe.print_nums_board()
    current_player = None
    while tic_tac_toe.empty_spots():
        if not current_player:
            # Choosing random player for the first move
            current_player = random.choice([player_1, player_2])
        else:
            # Alternating each player
            current_player = player_1 if current_player.avatar == player_2.avatar else player_2

        spot = current_player.get_move(tic_tac_toe)

        if tic_tac_toe.make_spot_owned(spot, current_player.avatar):
            print(f'Player {current_player.avatar} chooses {spot}\n')
            tic_tac_toe.print_board()

        if tic_tac_toe.winner :
            print(f'\nCongratulation player {current_player.avatar}! You won!')
            return current_player.avatar
        
        time.sleep(1)
    
    print('\nIt\'s a tie! Nice try guys!')

if __name__ == '__main__':
    game_intro()
    player_1, player_2 = create_player(choose_mode())
    tic_tac_toe = TicTacToe()
    play_game(tic_tac_toe, player_1, player_2)

    