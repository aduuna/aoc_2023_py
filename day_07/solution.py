from functools import cmp_to_key

def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    for i, row in enumerate(data):
        row = row.strip().split()
        data[i] = (row[0], int(row[1]))
    return data
    
def get_type(hand, with_joker=False):
    score = 7
    labels = {}
    for label in hand:
        labels[label]= labels[label]+1 if labels.get(label) else 1
    
    if with_joker:
        
        if (joker := labels.get('J')) and labels['J'] < 5:
            del labels['J']
            label, count = max(labels.items(), key=lambda x: x[1])
            labels[label] = count + joker

    counts = labels.values()
    match len(labels):
        case 1:
            return 7
        case 2:
            return 6 if 4 in counts else 5
        case 3:
            return 4 if 3 in counts else 3
        case 4:
            return 2
        case 5:
            return 1

def sort_key(item, other, with_joker=False):
    LABEL_ORDER =  '23456789TJQKA' if not with_joker else 'J23456789TQKA'
    item = item[0]
    other = other[0]
    t1, t2, = get_type(item, with_joker), get_type(other, with_joker)
    if t1 > t2:
        return 1
    if t1 < t2:
        return -1
    else:
        for a,b in zip(item, other):
            if LABEL_ORDER.index(a) > LABEL_ORDER.index(b):
                return 1
            if LABEL_ORDER.index(a) < LABEL_ORDER.index(b):
                return -1
        return 0
        

def part_1(data):
    total = 0
    hands = sorted(data, key=cmp_to_key(sort_key))
    rank=1
    for hand, bid in hands:
        print(hand, bid, rank*bid)
        total += rank*bid
        rank+=1
    return total



def part_2(data):
    total = 0
    sort_key_with_joker = lambda x, y: sort_key(x,y, with_joker=True)
    hands = sorted(data, key=cmp_to_key(sort_key_with_joker))
    rank=1
    for hand, bid in hands:
        # print(get_type(hand, True), hand, 'bid', bid, 'rank', rank, '*=', rank*bid)
        total += rank*bid
        rank+=1
    return total

if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)