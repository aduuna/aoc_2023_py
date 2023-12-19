import re, os, pathlib
from pprint import pprint
from functools import partial

def read_data(file="input.txt"):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    new_data = {'workflows': {}, 'ratings': []}
    is_workflow = True
    for row in data:
        row = row.strip()
        if row == '':
            is_workflow = False
            continue
        if is_workflow:
            k, v = row.split('{')
            new_data['workflows'][k] = v[:-1].split(',')
        else:
            row = row.lstrip('{').rstrip('}').split(',')
            ratings = {}
            for rating in row:
                k, v = rating.split('=')
                ratings[k] = int(v)
            new_data['ratings'].append(ratings)

    return new_data

def apply_condition(op, cat, val, action, rating):
    if op == '>':
        f = lambda cat, val, action, rating: action if rating[cat] > int(val) else None
    else:
        f = lambda cat, val, action, rating: action if rating[cat] < int(val) else None
    return f(cat, val, action, rating)

def workflow_to_lambda(workflow) :
    result = []
    for step in workflow:
        m = re.match(r'(?P<condition>(?P<category>\w{1})(?P<operator>[\<|\>])(?P<val>\d+):)?(?P<action>\w+)', step)
        if m.group('condition'):
            _, cat, op, val, action = m.groups()
            
            f = partial(apply_condition, op, cat, val, action)
        else:
            f = lambda rating: m.group("action")
        result.append(f)
    
    return result
        

def part_1(data):
    accepted = []
    workflows = {}
    for k, workflow in data['workflows'].items():
        workflows[k] = workflow_to_lambda(workflow)
    
    for rating in data['ratings']:
        action = None
        entry_point = 'in'
        while action != 'A' and action!='R':
            for rule in range(len(workflows[entry_point])):
                rule = workflows[entry_point][rule]
                if action:=rule(rating):
                    if action in ['A', 'R']:
                        if action =='A': accepted.append(rating)
                    else:
                        entry_point = action
                    break
    result = {'x': 0, 'm': 0, 'a':0, 's':0}
    for r in accepted:
        for k,v in r.items():
            result[k] += v
    
    return sum(result.values()) 


def part_2(data):
    result = {
        'x' : [(0, 4000, 'in')],
        'm' : [(0, 4000, 'in')],
        'a' : [(0, 4000, 'in')],
        's' : [(0, 4000, 'in')]
    }

    # action =  None
    # while action != 'A' and action!='R':



    # for workflow in data['workflows'].items():
    #     print(workflow)
    #     part_rating_range = rating[cat]
    #     for chunk in part_rating_range:
    #         c_min, c_max = chunk
    #         a, b = (c_min, val-1)(val, c_max) if op=='<' else (c_min, val) (val+1, c_max)
            

    return sum([v[1]-v[0] for v in sum(result.values(), [])])

if __name__ == '__main__':

    part_1_ans = part_1(read_data())
    print("Part 1 answer =>", part_1_ans)

    part_2_ans = part_2(read_data())
    print("Part 2 answer =>", part_2_ans)