from utils.reader import read_file

strategy_guide = read_file('inputs/day-2.txt')

rules_a = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},  # rock, paper win
    'B': {'X': 0, 'Y': 3, 'Z': 6},  # paper, scissors win
    'C': {'X': 6, 'Y': 0, 'Z': 3}  # scissors, rock win
}

rules_b = {
    'A': {3: 'X', 6: 'Y', 0: 'Z'},  # rock, paper win
    'B': {0: 'X', 3: 'Y', 6: 'Z'},  # paper, scissors win
    'C': {6: 'X', 0: 'Y', 3: 'Z'}  # scissors, rock win
}

shape_score = {
    'X': 1,  # lose
    'Y': 2,  # draw
    'Z': 3   # win
}

strategy_b = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6   # win
}


score_a = 0
score_b = 0
for strategy in strategy_guide:
    if strategy != '\n':
        game_round = strategy.split()
        score_a += rules_a[game_round[0]][game_round[1]] + shape_score[game_round[1]]
        s1 = strategy_b[game_round[1]]
        s2 = shape_score[rules_b[game_round[0]][s1]]
        score_b += s1 + s2

print(f'score A : {score_a}')
print(f'score A : {score_b}')
