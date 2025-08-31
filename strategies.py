'''Strategies for prisoner's dilemma.'''


import numpy as np


# move convention: int 0 = cooperate
def cooperate():
    return 0

# move convention: int 1 = defect
def defect():
    return 1

# always cooperate
def always_cooperate(opponent_moves):
    return cooperate()

# always defect
def always_defect(opponent_moves):
    return defect()

# cooperate or defect randomly (with equal probability)
def half_coop_half_defect(opponent_moves):
    return np.random.choice([cooperate(), defect()], p=[0.5, 0.5])

# tit-for-tat
def tit_for_tat(opponent_moves):
    # cooperate on first turn
    if not opponent_moves:
        return cooperate()
    # copy opponent's last move
    else:
        return opponent_moves[-1]



