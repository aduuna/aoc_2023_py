import os, pathlib, sys
from pprint import pformat, pprint
from functools import partial


def read_data(file="input.txt"):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    with open(file) as f:
        data = [line.strip().split() for line in f.readlines()]
    # basic clean up here

    return data

def is_within_bounds(trench, x_range, y_range, terrain):
    x, y = trench
    if 0<=x<x_range and 0<=y<y_range and terrain[y][x]=='.':
        return True
    return False


def get_next(terrain, visited):
    y = 1
    for x in range(len(terrain[0])):
        if '.' == terrain[y][x] and (x, y) not in visited and terrain[y][x-1]=='#':
            yield x, y

def find_area(start_trench, visited, terrain):
    area = set()
    trenches = {start_trench}
    x_range, y_range = len(terrain[0]), len(terrain)
    _is_safe = partial(is_within_bounds, x_range=x_range, y_range=y_range, terrain=terrain)
    is_safe = lambda x: x not in visited and _is_safe(x)
    while trenches:
        trench = trenches.pop()
        if trench in visited:
            continue
        visited.add(trench)
        x, y = trench
        trenches.update(list(filter(is_safe, [(x+1, y), (x-1, y), (x, y-1), (x, y+1)])))
        area.add(trench)
    return area


def find_bounded_region(terrain):
    visited = set()
    trench_gen = get_next(terrain, visited)

    while start_trench:=next(trench_gen, None):
        trench_region = find_area(start_trench, visited, terrain)
        if trench_region:
            break
    return trench_region


def part_1(data):
    lagoon = {(0, 0): '.'}
    x, y = 0, 0
    for dig_plan in data:
        direction, meters, color = dig_plan
        meters = int(meters)
        if direction in ['R', 'L']:
            start = x
            x += meters if direction=='R' else -meters
            x_range = range(start, x+1) if direction=='R' else range(x, start)
            lagoon.update({(x, y): '#' for x in x_range})
        else:
            start = y
            y += meters if direction=='D' else -meters
            y_range = range(start, y+1) if direction=='D' else range(y, start)
            lagoon.update({(x, y): '#' for y in y_range})
    l = lagoon.keys()
    key_x = lambda x: x[0]
    key_y = lambda y: y[1]
    bounds = [min(l, key=key_x)[0], max(l, key=key_x)[0], min(l, key=key_y)[1], max(l, key=key_y)[1]]
    x_min, x_max, y_min, y_max = bounds
    
    # fix scale to star from zero
    x_max = x_max+abs(x_min)
    y_max = y_max+abs(y_min)
    lagoon = {(a+abs(x_min), b+abs(y_min)): '#' for a,b in lagoon.keys()}

    terrain = [list(range(0, x_max+1)) for i in range(0, y_max+1)]
    for y in range(0, y_max+1):
        for x in range(0, x_max+1):
            if (x, y) in lagoon:
                terrain[y][x] = '#'
            else:
                terrain[y][x] = '.'
    # pprint(["".join(row) for row in terrain])
            
    bouned_trench = find_bounded_region(terrain)
    for trench in bouned_trench:
        x, y = trench
        terrain[y][x] = '#'
    # pprint(["".join(row) for row in terrain])
    return len(bouned_trench)+len(lagoon)

def part_2(data):
    m = {'0':'R', '1': 'D', '2' : 'L', '3' : 'U'}
    perim = 2
    lagoon = [(0,0)]
    x, y = 0, 0
    for dig_plan in data:
        _, _, color = dig_plan
        meters, direction = int(color[2:-2], base=16), m[color[-2]]
        if direction in ['R', 'L']:
            x += meters if direction=='R' else -meters
            lagoon.append((x,y))
        else:
            y += meters if direction=='D' else -meters
            lagoon.append((x,y))
        perim += meters

    # print(lagoon)
    lagoon.pop()
    
    area = 0
    n = len(lagoon)
    for i in range(1, n):
        area+= (lagoon[i-1][0]*lagoon[i][1]) - (lagoon[i][0]*lagoon[i-1][1])

    return abs(area)//2 +perim//2

if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)