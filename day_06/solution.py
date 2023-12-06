import math


def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    return data
    
def part_1(data):
    time, distance = [map(int, string.split(':')[1].strip().split()) for string in data]
    data = zip(time, distance)
    number_of_ways = []
    for race in data:
        win_counts = 0
        time, distance = race
        for charge_time in range(1, time):
            travelled_distance = charge_time * (time - charge_time)
            if travelled_distance > distance:
                win_counts += 1
        number_of_ways.append(win_counts)

    return math.prod(number_of_ways)
        
def part_2(data):
    time, distance = [int(string.split(':')[1].strip().replace(' ','')) for string in data]
    win_counts = 0
    for charge_time in range(1, time):
        travelled_distance = charge_time * (time - charge_time)
        if travelled_distance > distance:
            win_counts += 1
    
    return win_counts



if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)