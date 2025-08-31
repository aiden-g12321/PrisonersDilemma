'''Rules for prisoner's dilemma game.'''

import numpy as np
from player import Player


class Game:

    def __init__(self,
                 player1: Player,
                 player2: Player,
                 reward_matrix,
                 num_turns):
        
        self.player1 = player1
        self.player2 = player2
        self.player_list = [self.player1, self.player2]
        self.player1_moves = []
        self.player2_moves = []
        self.reward_matrix = reward_matrix
        self.num_turns = num_turns
        self.score = np.zeros(2)


    # single turn of game
    def turn(self):
        # get moves for this turn
        player1_move = self.player1.do_turn(self.player2_moves)
        player2_move = self.player2.do_turn(self.player1_moves)
        # update score from reward matrix
        self.score += self.reward_matrix[player1_move, player2_move]
        # update history of player moves
        self.player1_moves.append(player1_move)
        self.player2_moves.append(player2_move)


    # play game
    def play_game(self):
        _ = [self.turn() for _ in range(self.num_turns)]
        

    # get winner and loser of game
    def tally_score(self, print_results=False):
        # update players total scores
        for player, score_val in zip(self.player_list, self.score):
            player.total_score += score_val
    
        # check for a tie
        tie = self.score[0] == self.score[1]
        if tie:
            self.player1.tie_count += 1
            self.player2.tie_count += 1
            if print_results:
                print(f'{self.player1.name} tied {self.player2.name}.')
                print(f'score = {np.sort(self.score)}')
            
        # not a tie
        else:
            winner_index = np.argmax(self.score)
            winner = self.player_list[winner_index]
            loser = self.player_list[(winner_index + 1) % 2]
            # update win / loss count
            winner.win_count += 1
            loser.loss_count += 1
            if print_results:
                print(f'{winner.name} defeated {loser.name}.')
                print(f'score = {np.sort(self.score)[::-1]}.')
    
