def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here

    return data
    

def is_digit(char):
    try:
        int(char)
    except ValueError:
        return False
    return True

def part_1(data):
    nums = []
    for line in data:
        first, last = None, None
        for char in line:
            if is_digit(char):
                if not first:
                    first = char
                last = char
        nums.append(int(first+last))
    
    return sum(nums)
        
        
            
            
            

def part_2(data):
    pass

if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)