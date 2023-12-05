def read_data(file="input.txt"):
    with open(file) as f:
        seeds = f.readline().strip()
        data = []
        category = []
        for line in f.readlines():
            line = line.strip()
            if line == '':
                #new category
                if category: data.append(category)
                category = []
            elif category:
                category[1].append(line)
            else:
                category = [line, []]
        data.append(category)

    categories = []
    for category in data:
        categories.append(CategoryMap(*category))
                
    return [seeds]+categories
    
class CategoryMap():
    def __init__(self, name: str, map_data: list) -> None:
        self.name = name.strip(' map:')
        self.source_name, self.destination_name = self.name.split("-to-")
        self.map_data = map_data
        # self.map_cache = {}
    
    def get_destination_ranges(self, source_start, source_range_length):
        # source_range = source_start, source_start+range_length
        print(self)
        destination_ranges = []
        for row in self.map_data:
            print(row)
            map_destination_start, map_source_start, map_range_length = [int(x) for x in row.split()]
            if map_source_start <= source_start < map_source_start+map_range_length:
                # map entire range to out put
                print("appending head overlap")
                offset = source_start - map_source_start
                destination_ranges.append([map_destination_start+offset, min(source_range_length, map_range_length)])
                print(destination_ranges)
            elif source_start <= map_source_start < source_start+source_range_length:
                print("appending tail overlap")
                offset = source_start - map_source_start
                destination_ranges.append([map_destination_start, min(map_range_length, source_range_length)+offset])
                print(destination_ranges)
        
   
        return sorted(destination_ranges)
        
    def get_destination(self, source):
        # return self.map_cache.get(source_number) or self._get_from_map_data(source_number)
        destination = source # default
        for row in self.map_data:
            map_destination_start, map_source_start, map_range_length = [int(x) for x in row.split()]
            if map_source_start <= source < map_source_start+map_range_length:
                destination = map_destination_start + (source - map_source_start)
                break
        # self.map_cache[source_number] = destination_number
        return destination
    
    def __repr__(self):
        string = f"{{Category <{self.name}> data={self.map_data}}}"
        return string


def part_1(data):
    seeds = [int(x) for x in data[0].split(':')[-1].strip().split()]

    locations = []
    for seed in seeds:
        source = seed # start_point
        for category in data[1:]:
            destination = category.get_destination(source)

            source = destination # use destination as source for next category
        # print('seed', seed, 'final_destination', destination_number)
        locations.append(destination)

   
    return min(locations)


def part_2(data):
    seeds = [int(x) for x in data[0].split(':')[-1].strip().split()]
    categories = data[1:]
    locations = []
    for i in range(0, len(seeds), 2):
        start, range_length = seeds[i], seeds[i+1]
        ranges = [ [start, range_length] ]
        print("starting processing", ranges)
        for category in categories:
            for source_range in ranges:
                ranges.pop(0)
                destination_ranges = category.get_destination_ranges(*source_range)
                ranges.extend(destination_ranges)

        locations.extend(ranges)
        print(locations)
    return None

if __name__ == '__main__':
    data = read_data()

    part_1 = part_1(data)
    print("Part 1 answer =>", part_1)

    part_2 = part_2(data)
    print("Part 2 answer =>", part_2)