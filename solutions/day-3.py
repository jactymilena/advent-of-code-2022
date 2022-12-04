import string
from utils.reader import read_file


def to_dictionary(rucksacks):
    occurrences = {}
    for r in rucksacks:
        occurrences[r] = 1

    return occurrences


letters = {}
for i, c in enumerate(string.ascii_letters):
    letters[c] = i + 1

lines = read_file('inputs/day-3.txt')
priority = 0
for line in lines:
    size = int(((len(line) - 1) / 2))
    rucksacks1 = line[0:size]
    rucksacks2 = line[size:size * 2]

    oc1 = to_dictionary(rucksacks1)
    oc2 = to_dictionary(rucksacks2)
    priority += letters[list(oc1.keys() & oc2.keys())[0]]

print(f'priority {priority}')
