def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    for row in range(len(data)):
        data[row] = data[row].strip()

    return data
    
def get_start(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return i,j

def get_tile(data, pos):
    row, col = pos
    if row==-1 or col==-1 or row>=len(data) or col>=len(data[row]):
        return None
    return data[row][col]


def match(data, tile1, tile2):
    ALL = '|-LJ7F'
    horizontal_connections = ['LJ', 'FJ', 'L7', 'F7', '--', 'F-', '-7', '-J', 'L-']
    vertical_connections   = ['L7', 'LF', 'JF', 'J7', '||', '|F', '|7', 'J|', 'L|']
    diff = (tile1[0] - tile2[0], tile1[1] - tile2[1])
    connection: str = get_tile(data, tile1) + get_tile(data, tile2)
    if 'S' in connection:
        connection = connection.replace('S', '|') if diff in [(1, 0), (-1, 0)] else connection.replace('S', '-') 
    # print('connection', connection, tile1, tile2)
    if diff == (1, 0):
        return connection in vertical_connections
    elif diff == (-1, 0):
        return connection[::-1] in vertical_connections
    elif diff == (0, -1):
        return connection in horizontal_connections
    elif diff == (0, 1):
        return connection[::-1] in horizontal_connections


def get_next(data, visited, tile):
    matches = []
    row, col = tile
    neighbours = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    # print("working with", tile, neighbours)
    for neighbour in neighbours:
        if get_tile(data, neighbour) in [None, '.']:
            continue
        if neighbour in visited:
            continue
        if match(data, tile, neighbour):
            matches.append(neighbour)
    # print("tile, matches =>", tile, matches)
    return matches
    

def part_1(data, return_path=False):
    start = get_start(data)
    visited = [start]
    paths = get_next(data, visited,  start)
    # print('paths', paths)
    farthest = 0
    for path in paths:
        visited = [start]
        queue = [path]
        depth = 1
        # visited = [[0]*len(i) for i in data]
        while queue!=[]:
            tile = queue.pop(0)
            queue += get_next(data, visited, tile)
            visited.append(tile)
            depth += 1
        if depth > farthest:
            farthest = depth
            final_path = visited
    
    # used for part2
    if return_path:
        return final_path

    return (farthest+1)//2


def part_2(data):
    path =  part_1(data, return_path=True)
    area = [['.']*len(i) for i in data]
    for tile in path:
        row, col = tile
        area[row][col] = '0'

    import pprint
    pprint.pprint(area)


if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)