from utils.reader import read_file

calories = read_file('inputs/day-1.txt')

calories_sum = 0
max_calories = 0

for calorie in calories:
    if calorie != '\n':
        calories_sum += int(calorie)
    else:
        max_calories = max(calories_sum, max_calories)
        calories_sum = 0

print(f'max calories : {max_calories}')

