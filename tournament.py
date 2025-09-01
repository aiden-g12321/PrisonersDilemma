'''Tournament of prisoner's dilemma between multiple players.'''


from player import Player
from game import Game
from typing import List


class Tournament:

    def __init__(self, players: List[Player], point_matrix, num_turns):
        self.players = players
        self.num_players = len(self.players)
        self.games = {}
        self.point_matrix = point_matrix
        self.num_turns = num_turns

    def play_tournament(self):
        for i in range(self.num_players):
            for j in range(i, self.num_players):
                game = Game(self.players[i], self.players[j],
                            self.point_matrix, self.num_turns)
                game.play_game()
                game.tally_score()
                self.games[(self.players[i].name, self.players[j].name)] = game
                self.games[(self.players[j].name, self.players[i].name)] = game
