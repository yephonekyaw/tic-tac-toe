import math, random


class Player():
    def __init__(self, avatar):
        self.avatar = avatar
    

class HumanPlayer(Player):
    def __init__(self, avatar):
        super().__init__(avatar)
    
    def get_move(self, tic_tac_toe):
        spot = None
        valid_spot = False
        while not valid_spot:
            spot = input(f'\n{self.avatar}\'s turn. Enter your spot(0-9): ')
            try:
                spot = int(spot)
                if spot not in tic_tac_toe.available_spots():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('\nInvalid spot. Try again!')
        return spot


class ComputerPlayerEsay(Player):
    def __init__(self, avatar):
        super().__init__(avatar)

    def get_move(self, tic_tac_toe):
        spot = random.choice(tic_tac_toe.available_spots())
        print(f'\nComputer({self.avatar})\'s turn!')
        return spot


class ComptuerPlayerImpossible(Player):
    def __init__(self, avatar):
        super().__init__(avatar)

    def get_move(self, tic_tac_toe):
        print(f'\nComputer({self.avatar})\'s turn!')
        if len(tic_tac_toe.available_spots()) == 9:
            spot = random.choice(tic_tac_toe.available_spots())
        else:
            spot = self.minimax(tic_tac_toe, self.avatar, 0)['position']
        return spot

    def minimax(self, tic_tac_toe, current_player, depth):
        max_player = self.avatar
        # other_player will be current_player in the next round
        # as well as current_player in the last round
        # to check if the last round was a terminal end
        other_player = 'O' if current_player == 'X' else 'X'
        if tic_tac_toe.winner == other_player:
            return {'position': None, 'score': (10 - depth) if other_player == max_player else (-10 + depth)}
        elif not tic_tac_toe.empty_spots():
            return {'position': None, 'score': 0}

        if current_player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for avail_spot in tic_tac_toe.available_spots():
            tic_tac_toe.make_spot_owned(avail_spot, current_player)
            tem_score = self.minimax(tic_tac_toe, other_player, depth + 1)

            tic_tac_toe.board[avail_spot] = ' '
            tic_tac_toe.winner = None
            tem_score['position'] = avail_spot

            # compare and find the min or max score
            if current_player == max_player:
                if tem_score['score'] > best['score']:
                    best = tem_score
            else:
                if tem_score['score'] < best['score']:
                    best = tem_score
        return best



        
