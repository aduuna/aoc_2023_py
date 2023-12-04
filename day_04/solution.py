from math import pow


def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    for i, line in enumerate(data):
        line = line.split(':')[1]
        line = [sorted(map(int, numbers.strip().split())) for numbers in line.split('|')]
        data[i] = line

    return data
    

def part_1(data):
    total = 0
    for card in data:
        count = 0
        winning_numbers, player_numbers = card
        for num in winning_numbers:
            for p_num in player_numbers:
                if num == p_num:
                    count+=1
                    break
                elif p_num > num:
                    break
        total += int(pow(2, count-1)) if count>0 else 0
    return total


def part_2(data):
    total_cards = {}
    for i, card in enumerate(data, 1):
        count = 0
        total_cards[i] = total_cards[i]+1 if total_cards.get(i) else 1
        
        for num in card[0]:
            if num in card[1]:
                count += 1

        if count == 0:
            continue

        for j in range(i+1, count+i+1):
            total_cards[j] = total_cards[j]+total_cards[i] if total_cards.get(j) else total_cards[i]


    return sum(total_cards.values())

if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)