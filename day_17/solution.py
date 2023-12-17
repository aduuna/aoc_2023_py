def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here

    return data
    

def part_1(data):
    pass

def part_2(data):
    pass

if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)