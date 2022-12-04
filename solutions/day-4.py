from utils.reader import read_file


def is_between(p1, p2):
    return (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p2[0] <= p1[0] and p2[1] >= p1[1])


pairs = read_file('inputs/day-4.txt')

fc = 0
for pair in pairs:
    sp = pair.strip().split(',')

    first = list(map(int, sp[0].split('-')))
    second = list(map(int, sp[1].split('-')))

    fc += 1 if is_between(first, second) else 0

print(fc)
