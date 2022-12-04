from utils.reader import read_file

calories = read_file('inputs/day-1.txt')

calories_sum = 0
max_calories = []

for calorie in calories:
    if calorie != '\n':
        calories_sum += int(calorie)
    else:
        max_calories.append(calories_sum)
        calories_sum = 0

max_calories.sort(reverse=True)
print(f'max calories : {max_calories[0:3]}')
print(f'total max calories : {sum(max_calories[0:3])}')

