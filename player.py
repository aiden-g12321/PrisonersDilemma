'''Player object for prisoner's dilemma.'''


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
        self.personality = 'Nasty' if self.is_nasty() else 'Nice'

        self.win_count = win_count
        self.loss_count = loss_count
        self.tie_count = tie_count
        
        self.total_points = total_points

    # player makes move based on opponent's previous moves
    def do_turn(self, opponent_moves):
        return self.strategy(opponent_moves)
    
    # test if strategy is nasty (defects first)
    def is_nasty(self):
        nice_opponent_moves = [cooperate() for _ in range(10_000)]
        player_response = [self.do_turn(nice_opponent_moves[:i])
                           for i in range(len(nice_opponent_moves))]
        if defect() in player_response:
            return True
        else:
            return False
    

    