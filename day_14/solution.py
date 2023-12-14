import os, pathlib
from pprint import pprint 

def read_data(file="input.txt"):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    data = [row.strip() for row in data]

    return data
    

def tilt(column):
    for i in range(1, len(column)):
        if column[i] in ['.', '#']:
            continue
        j = i
        while  j != 0 and column[j-1] == '.':
            column[j-1], column[j] = column[j], column[j-1]
            j -= 1 
    return column


def part_1(data):
    # pprint(data)
    rotated_data = [[r[i] for r in data] for i in range(len(data[0]))]
    # pprint(rotated_data)
    for i in range(len(rotated_data)):
        col = tilt(rotated_data[i])
        rotated_data[i] = col
    
    total = 0
    for col in rotated_data:
        length = len(col)
        for i in range(length):
            if col[i] == 'O':
                total += length-i
    pprint(["".join([r[i] for r in rotated_data]) for i in range(len(rotated_data[0]))])
    return total
            

def part_2(data):
    #all directions, for 1, billion cycles
    pass

if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)