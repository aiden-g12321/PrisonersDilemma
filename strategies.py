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
def random(opponent_moves):
    return np.random.choice([cooperate(), defect()], p=[0.5, 0.5])

# tit-for-tat
def tit_for_tat(opponent_moves):
    # cooperate on first turn
    if not opponent_moves:
        return cooperate()
    # copy opponent's last move
    else:
        return opponent_moves[-1]
    
# tit-for-2-tats
def tit_for_2_tats(opponent_moves):
    # cooperate on first turn and second turn
    if not opponent_moves or len(opponent_moves) == 1:
        return cooperate()
    # if opponent defects twice in a row, then defect
    elif opponent_moves[-1] == defect() and opponent_moves[-2] == defect():
        return defect()
    # cooperate otherwise
    else:
        return cooperate()
    
# if opponent defects once, then always defects
def Friedman(opponent_moves):
    if defect() in opponent_moves:
        return defect()
    else:
        return cooperate()

# tit-for-tat but defect 10% of time
def Joss(opponent_moves, defect_rate=0.1):
    # cooperate first turn
    if not opponent_moves:
        return cooperate()
    else:
        # sometimes defect
        sneaky_defect = np.random.choice([True, False], p=[defect_rate, 1-defect_rate])
        if sneaky_defect:
            return defect()
        # otherwise tit-for-tat
        else:
            return tit_for_tat(opponent_moves)
        
# defect first round, if opponent retaliates then apologize and play tit-for-tat
def Tester(opponent_moves):
    # defect first round
    if not opponent_moves:
        return defect()
    # cooperate second round
    elif len(opponent_moves) == 1:
        return cooperate()
    else:
        # check if opponent retaliates
        opponent_is_pushover = opponent_moves[1] == cooperate()
        if opponent_is_pushover:  # defect every other round
            if len(opponent_moves) % 2 == 0:
                return defect()
            else:
                return cooperate()
        else:  # opponent if not pushover
            if len(opponent_moves) == 2:  # apologize
                return cooperate()
            else:
                return tit_for_tat(opponent_moves)



