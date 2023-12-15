from functools import reduce
import re

def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
        data = data[0].split(',')
    # basic clean up here

    return data

def special_hash(string):
    fun = lambda t, v: ((t+ord(v)) * 17) % 256
    return reduce(fun, string, 0)

def part_1(data):
    return sum([special_hash(step) for step in data])

def part_2(data):
    boxes = [{} for i in range(256)]
    for step in data:
        label, sep, count = re.match(r'(?P<label>\w+)(?P<sep>[-|=])(?P<count>.*)', step).groups()
        box = boxes[special_hash(label)]
        if sep == '-' and label in box:
            del box[label]
        elif sep == '=':
            box[label] = int(count)
    focusing_power = 0
    for i in range(len(boxes)):
        for j, k in enumerate(boxes[i]):
            focusing_power += (i+1) * (j+1) * boxes[i][k]

    return focusing_power


if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)