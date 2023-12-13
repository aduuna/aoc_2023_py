import os, pathlib
from pprint import pprint

def read_data(file="input.txt"):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    new_data = []
    temp = []
    for row in data:
        row = row.strip()
        if row == '':
            new_data.append(temp)
            temp = []
            continue
        temp.append(row)
    new_data.append(temp)

    return new_data
    

def find_reflection(pattern, vertical=False, with_smudge=False):
    # Todo: case where smudge is fake cos we are not on the true reflection line, we ned reset 
    # the smudge fix availble and go look for the true reflection line
    # Todo: case where a reflection is foumd but we havent fixed any smudge yet, every mirror must have exactly one smudge

     
    if vertical:
        pattern = ["".join([r[i] for r in pattern]) for i in range(len(pattern[0]))]


    for mirror_idx in range(1, len(pattern)):
        l_ptr, r_ptr = mirror_idx-1, mirror_idx
        symmetric = False
        total_diff = 0

        while l_ptr >= 0 and r_ptr<len(pattern):
            
            diff = len(list(filter(lambda x: x[0]!=x[1], zip(pattern[l_ptr], pattern[r_ptr]))))
            is_reflection = diff <= 1 if with_smudge else diff == 0

            if is_reflection:
                total_diff += diff
                symmetric = True
                r_ptr += 1
                l_ptr -= 1 
            else:
                symmetric = False
                break
        if symmetric:
            if with_smudge:
                if total_diff == 1: break
                else: symmetric= False; continue
            break  

    count =  mirror_idx if symmetric else 0

    return count if vertical else 100*count

def part_1(data, with_smudge=False):
    total = 0
    for pattern in data:
        if not (reflections:=find_reflection(pattern, vertical=False, with_smudge=with_smudge)):
            reflections = find_reflection(pattern, vertical=True, with_smudge=with_smudge)
        if with_smudge:
            if not reflections:
                pass
        total += reflections

    return total      

def part_2(data):
    return part_1(data, with_smudge=True)


if __name__ == '__main__':

    part_1_ans = part_1(read_data())
    print("Part 1 answer =>", part_1_ans)

    part_2_ans = part_2(read_data())
    print("Part 2 answer =>", part_2_ans)