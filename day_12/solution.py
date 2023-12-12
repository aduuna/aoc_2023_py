from math import perm, factorial

def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    data = [i.strip().split() for i in data]
    return data
    

def get_conditions(springs, condition):
    unknowns = []
    for i, _ in enumerate(springs):
        if _==condition: unknowns.append(i)
    return unknowns

def part_1(data):
    total = 0
    for springs, contiguous_damaged in data:
        permutations = 0
        contiguous_damaged = list(map(int,contiguous_damaged.split(',')))
        unknowns = get_conditions(springs, '?')
        damaged = get_conditions(springs, '#')
        operational = get_conditions(springs, '.')
        for i in range(len(contiguous_damaged)):
            # a = contiguous_damaged[:i]
            # b = contiguous_damaged[i]
            # c = contiguous_damaged[i+1:]
            # a, c = sum(x) + len(x)
            # springs[:-n]
            pass


def part_2(data):
    pass

if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)