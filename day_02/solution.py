from math import prod

def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    get = lambda x: x.strip().split()[::-1]
    for i in range(len(data)):
        data[i] = data[i].split(':')[1]
        draws = data[i].split(';')
        for j in range(len(draws)):
            draws[j] = {get(x)[0]: int(get(x)[1]) for x in draws[j].split(',')}
        data[i] = draws
    return data
    

def part_1(data):
    configurations = {
        'red' : 12,
        'green': 13,
        'blue': 14,
        }
    possible_games = []
    for game in range(len(data)):
        possible = True
        for draw in data[game]:
            for color, count in draw.items():
                if count > configurations[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_games.append(game+1)
    
    print(possible_games)
    return sum(possible_games)



def part_2(data):
    power_prod = 0
    for game in data:
        fewest_required = {
            'red' : 0,
            'green': 0,
            'blue': 0,
        }
        for draw in game:
            for color, count in draw.items():
                if count > fewest_required[color]:
                    fewest_required[color] = count
        power_prod += prod(fewest_required.values())
    return power_prod

if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)