from math import prod
from pprint import pprint


def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    data = [line.strip() for line in data]

    return data

digits = '0123456789'


def get(data, row, col):
    if row==-1 or col==-1:
        return None
    try:
        return data[row][col]
    except IndexError:
        return None
    
def get_adjacents(data, row, start, end):
    adjacents = []
    #check above, top adjacents, below and bottom adjacents, left and right
    for col in range(start-1, end+2):
        if val:= get(data, row-1, col):
            adjacents.append(val)
        if val:= get(data, row, col):
            adjacents.append(val)
        if val:= get(data, row+1, col):
            adjacents.append(val)
    return adjacents
    
def has_symbol_adjacents(data, row, start, end):
    adjacents = get_adjacents(data, row, start, end)

    for val in adjacents:
        if val not in digits+'.':
            return True
    return False

def has_star_adjacents(data, row, start, end):
    star_positions = []
    for col in range(start-1, end+2):
        if val:= get(data, row-1, col):
            if val=='*': star_positions.append((row-1, col))
        if val:= get(data, row, col):
            if val=='*': star_positions.append((row, col))
        if val:= get(data, row+1, col):
            if val=='*': star_positions.append((row+1, col))
    return star_positions

def has_two_part_numbers(data, row, col):
    pass

def part_1(data):
    # loop through all the entries
    #find an engine number in whole, with its index
    # look around the adjacents for a symbol .i.e non-digit, non-dot
    #if a single symbol is found, keep as part_number
    #sum all part numbers
    part_numbers = []
    for i in range(len(data)):
        row = data[i]
        j = 0
        current_number = ''
        pos_start, pos_end = None, None
        while j < len(row):
            if row[j] in digits:
                current_number += row[j]
                pos_start = pos_start if pos_start != None else j

            elif pos_start!=None:
                pos_end = j-1

                if has_symbol_adjacents(data, i, pos_start, pos_end):
                    part_numbers.append(int(current_number))
                current_number = ''
                pos_start, pos_end = None, None


            j += 1
        if pos_start!=None and current_number:
            if has_symbol_adjacents(data, i, pos_start, j-1):
                part_numbers.append(int(current_number))

    return sum(part_numbers)

def part_2(data):
    gear_ratios = []
    gear_map = {}
    for i in range(len(data)):
        row = data[i]
        j = 0
        current_number = ''
        pos_start, pos_end = None, None
        while j < len(row):
            if row[j] in digits:
                current_number += row[j]
                pos_start = pos_start if pos_start != None else j

            elif pos_start!=None:
                pos_end = j-1
                if star_adjacents:=has_star_adjacents(data, i, pos_start, pos_end):
                    for pos in star_adjacents:
                        gear_map[pos] = [int(current_number)] if pos not in gear_map else gear_map[pos]+[int(current_number)]
                current_number = ''
                pos_start, pos_end = None, None

            j += 1
        if pos_start!=None and current_number:
            if star_adjacents:=has_star_adjacents(data, i, pos_start, j-1):
                for pos in star_adjacents:
                    gear_map[pos] = [int(current_number)] if pos not in gear_map else gear_map[pos]+[int(current_number)]


    for gear, part_numbers in gear_map.items():
        if len(part_numbers) == 2:
            gear_ratios.append(prod(part_numbers))            
    return sum(gear_ratios)

if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)