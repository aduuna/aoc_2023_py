def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    for i in range(len(data)):
        data[i] = [int(x) for x in data[i].strip().split()]
    return data
    

def extrapolate(seq: list, pos: int):
    diffs = [seq[i]-seq[i-1] for i in range(1,len(seq))]
    if pos==-1:
        return seq[-1] if diffs==[0]*len(diffs) else seq[-1] + extrapolate(diffs, -1)
    elif pos==0:
        return seq[0] if diffs==[0]*len(diffs) else seq[0] - extrapolate(diffs, 0)
 
def part_1(data):
    total = 0
    for seq in data:
        total += extrapolate(seq, -1)
    return total

def part_2(data):
    total = 0
    for seq in data:
        total += extrapolate(seq, 0)
    return total

if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)