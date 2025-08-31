'''Player object for prisoner's dilemma.'''


import numpy as np
from strategies import cooperate, defect


class Player:

    def __init__(self,
                 strategy,
                 win_count=0,
                 loss_count=0,
                 tie_count=0,
                 total_points=0.):
        
        self.strategy = strategy
        self.name = self.strategy.__name__.upper()
        self.is_nasty = self.test_if_nasty()
        self.is_retaliatory = self.test_if_retaliatory()

        self.win_count = win_count
        self.loss_count = loss_count
        self.tie_count = tie_count
        
        self.total_points = total_points

    # player makes move based on opponent's previous moves
    def do_turn(self, opponent_moves):
        return self.strategy(opponent_moves)
    
    # test if strategy is nasty (defects first)
    def test_if_nasty(self):
        nice_opponent_moves = [cooperate() for _ in range(10_000)]
        player_response = [self.do_turn(nice_opponent_moves[:i])
                           for i in range(len(nice_opponent_moves))]
        if defect() in player_response:
            return True
        else:
            return False
        
    # test if strategy is retaliatory (immediately strikes back)
    def test_if_retaliatory(self):
        # opponent sometimes defects
        opponent_moves = np.random.choice(np.array([defect(), cooperate()]),
                                          size=(10_000),
                                          p=[0.1, 0.9])
        defect_indices = np.where(opponent_moves[:-1] == defect())[0]
        player_response = np.array([self.do_turn(opponent_moves[:i])
                                    for i in range(len(opponent_moves))])
        # check responses to defects
        response_to_defects = player_response[defect_indices + 1]
        if np.any(response_to_defects == cooperate()):
            return False
        else:
            return True
        
        
    

    