def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    nav, _ = data.pop(0).strip(), data.pop(0)
    Node.nodes = set()
    for i, row in enumerate(data):
        node, children = row.replace(' ', '').strip().split('=')
        # print(node, children)
        data[i] = Node(node, children.strip("()").split(','))

    return [nav]+data  
  
class Node:
    nodes = set()

    def __init__(self, node, children) -> None:
        self.id = node
        if children: self.set_children(children)
        Node.nodes.add(self)


    def __new__(cls, node, children):
        instance = super().__new__(cls)
        # print(node, end=' ')
        if node:=cls.get_node(node):
            # print('exists')
            return node
        # print('new')
        return instance
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __repr__(self):
        string = f"{self.id} "
        if self.L:
            string += f"({self.L.id}, {self.R.id})" if self.L.id!=self.id else f"({self.id}, {self.id})"

        return string

    @classmethod
    def get_node(cls, node):
        node_id = node if type(node)==str else node.id
        for i in cls.nodes:
            if i.id == node_id:
                return i
        return None
    
    def set_children(self, children):
        # print("setting children", children)
        self.L = Node(children[0], None) if children[0]!=self.id else self
        self.R = Node(children[1], None) if children[1]!=self.id else self

def part_1(data):
    navigations = data.pop(0)
    nav_length = len(navigations)
    current = Node.get_node('AAA')
    i = steps = 0
    while True:
            if current.id == 'ZZZ':
                print("found")
                return steps
            current = getattr(current, navigations[i])
            steps+=1
            i = i+1 if i+1 <= nav_length-1 else 0      


def part_2(data):
    navigations = data.pop(0)
    nav_length = len(navigations)
    current_nodes = []
    for node in Node.nodes:
        if node.id.endswith('A'):
            current_nodes.append(node)
    all_steps = []
    for current in current_nodes:
        i = steps = 0
        while True:
            if current.id.endswith('Z'):
                all_steps.append(steps)
                break
            current = getattr(current, navigations[i])
            steps+=1
            i = i+1 if i+1 <= nav_length-1 else 0 

    import math
    return math.lcm(*all_steps) 
    

if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)