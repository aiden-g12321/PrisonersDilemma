'''Player object for prisoner's dilemma.'''


class Player:

    def __init__(self, strategy, win_count=0, loss_count=0, tie_count=0):
        self.strategy = strategy
        self.name = self.strategy.__name__.upper()
        self.win_count = win_count
        self.loss_count = loss_count
        self.tie_count = tie_count

    def do_turn(self, opponent_moves):
        return self.strategy(opponent_moves)
    