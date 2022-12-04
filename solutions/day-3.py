import string
from utils.reader import read_file


def to_dictionary(rs):
    oc = {}
    for r in rs:
        oc[r] = 1

    return oc


letters = {}
for i, c in enumerate(string.ascii_letters):
    letters[c] = i + 1

lines = read_file('inputs/day-3.txt')
priority_one = 0
priority_two = 0
rucksacks = []
for i, line in enumerate(lines):
    # part one
    size = int(((len(line) - 1) / 2))
    rucksacks1 = line[0:size]
    rucksacks2 = line[size:size * 2]

    oc1 = to_dictionary(rucksacks1)
    oc2 = to_dictionary(rucksacks2)
    priority_one += letters[list(oc1.keys() & oc2.keys())[0]]

    # part two
    rucksacks.append(to_dictionary(line[0: len(line)-1]))
    print(line)
    if i % 3 == 2:
        inter = rucksacks[0].keys() & rucksacks[1].keys() & rucksacks[2].keys()
        priority_two += letters[list(inter)[0]]
        rucksacks.clear()

print(f'priority one {priority_one}')
print(f'priority two {priority_two}')
