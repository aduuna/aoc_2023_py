import pprint
from itertools import combinations

def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here

    return data

def expand(data):
    new_data: list[str] = []
    for i in range(len(data)):
        row = data[i].strip()
        new_data.append(row)
        if row == "."*len(row):
            new_data.append(row)
    
    col = 0
    while col < len(new_data[0]):
        column = [i[col] for i in new_data]
        # print('col', column)
        if column == ['.']*len(column):
            for row in range(len(new_data)):
                new_data[row] = new_data[row][:col] + new_data[row][col:].replace('.', '..', 1)
            col+=1
        col+=1
    return new_data

def get_expandables(data):
    expandable_rows = []
    expandable_cols = []
    for i in range(len(data)):
        data[i] = data[i].strip()
        if data[i] == "."*len(data[i]):
            expandable_rows.append(i)
    col = 0
    while col < len(data[0]):
        column = [i[col] for i in data]
        if column == ['.']*len(column):
            expandable_cols.append(col)
        col+=1
    return expandable_rows, expandable_cols

    
def find_galaxies(data):
    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                galaxies.append((i,j))

    return galaxies

def find_shortest_path(galaxy_1, galaxy_2):
    steps = abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])

    return steps

def span_expandable(galaxy_1, galaxy_2, rows, cols):
    count = 0
    for row in rows:
        if galaxy_1[0] < row < galaxy_2[0] or galaxy_2[0] < row < galaxy_1[0]:
            count += 1
    for col in cols:
        if galaxy_1[1] < col < galaxy_2[1] or galaxy_2[1] < col < galaxy_1[1]:
            count += 1
    return count


def part_1(data):
    data = expand(data)
    total = 0
    galaxies = find_galaxies(data)
    for galaxy_pair in combinations(galaxies, 2):
        total += find_shortest_path(*galaxy_pair)

    return total

def part_2(data, factor=1_000_000):
    expandable_rows, expandable_cols = get_expandables(data)
    print(expandable_rows, expandable_cols)
    total = 0
    galaxies = find_galaxies(data)
    for galaxy_pair in combinations(galaxies, 2):
        shortest_path = find_shortest_path(*galaxy_pair)
        if count:=span_expandable(*galaxy_pair, expandable_rows, expandable_cols):
            shortest_path = shortest_path + (factor*count) - count
        # print(galaxy_pair, shortest_path, count)
        total += shortest_path

    return total


if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)