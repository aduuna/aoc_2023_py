import os, pathlib
from pprint import pformat

def read_data(file="input.txt"):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    data = []
    with open(file) as f:
        [data.append(line.strip()) for line in f.readlines()]
    # basic clean up here

    return data
    
class TileType:
    Mirror_L = '/'
    Mirror_R = '\\'
    Splitter_H = '-'
    Splitter_V = '|'
    Empty_Space = '.'
    Mirror = Mirror_L, Mirror_R
    Splitter = Splitter_H, Splitter_V


class Direction:
    R = (1, 0)
    L = (-1, 0)
    U = (0, -1)
    D = (0, 1)


class Tile:
    def __init__(self, x, y, tile_type: str) -> None:
        self.x = x
        self.y = y
        self.energized = set()
        self.tile_type = tile_type

    def __repr__(self):
        # return str(self.tile_type)
        return '#' if len(self.energized)>=1 else '.'
    
    def __eq__(self, __value: object) -> bool:

        return __value and self.x == __value.x and self.y==__value.y
    
    def energize(self, beam):
        if beam.direction in self.energized:
            return False
        self.energized.add(beam.direction)
        return True

class Beam:
    def __init__(self, init_tile: Tile, direction: Direction) -> None:
        self.init_tile = init_tile
        current_tile = None
        self.direction = direction
        self.quenched = False
    
    def __repr__(self) -> str:
        return pformat(vars(self))
    
    def split(self):
        if self.current_tile.tile_type not in TileType.Splitter:
            return
        self.quenched = True

        if self.direction in [Direction.R, Direction.L] and self.current_tile.tile_type in TileType.Splitter_V:
            return Beam(init_tile=self.current_tile, direction=Direction.U), Beam(init_tile=self.current_tile, direction=Direction.D)
        elif self.direction in [Direction.U, Direction.D] and self.current_tile.tile_type in TileType.Splitter_H:
            return Beam(init_tile=self.current_tile, direction=Direction.L), Beam(init_tile=self.current_tile, direction=Direction.R)
        else:
            return [Beam(init_tile=self.current_tile, direction=self.direction)]
    
    def bounce(self):
        if self.current_tile.tile_type not in TileType.Mirror:
            return
        if self.current_tile.tile_type == TileType.Mirror_R:
            self.direction = self.direction[::-1]
        elif self.current_tile.tile_type == TileType.Mirror_L:
            self.direction = (-self.direction[1], -self.direction[0])

    def move_to(self, tile: Tile):
        if tile==None or (tile!=None and tile==self.init_tile):
            self.quenched = True
            return
        energized = tile.energize(self)
        if not energized and tile!=self.init_tile:
            self.quenched = True
            return
        self.current_tile = tile
        if self.current_tile.tile_type == TileType.Empty_Space:
            return
        elif self.current_tile.tile_type in TileType.Splitter:
            return self.split()
        elif self.current_tile.tile_type in TileType.Mirror:
            return self.bounce()
        


class Grid:
    def __init__(self, x_range, y_range, tiles: list[list[Tile]]) -> None:
        self.x_range = x_range
        self.y_range = y_range
        self.tiles = tiles
        self.beams = []

    def __repr__(self) -> str:
        return pformat(vars(self))
    
    def get_tile(self, x, y):
        if 0<=x<self.x_range and 0<=y<self.y_range:
            return self.tiles[y][x]
        
    
    def shoot_beam(self, beam: Beam):
        self.beams.append(beam)
        while self.beams:
            beam = self.beams.pop(0)
            x, y = beam.init_tile.x, beam.init_tile.y
            while not beam.quenched:
                x, y = x+beam.direction[0], y+beam.direction[1]
                tile = self.get_tile(x, y)
                split_beams = beam.move_to(tile)
                if split_beams:
                    self.beams.extend(split_beams)
    def get_energized_count(self):
        return len(list(filter(lambda t: t.energized, sum(self.tiles, []))))


def part_1(data, x=0, y=0, direction=Direction.R):
    tiles = [[Tile(i, j, data[j][i]) for i in range(len(data[j]))] for j in range(len(data))]
    grid = Grid(len(tiles[0]), len(tiles), tiles)
    beam = Beam(tiles[y][x], direction)
    beam.init_tile.energize(beam)
    grid.shoot_beam(beam)
    return grid, grid.get_energized_count()
        
    


def part_2(data):
    maximum  = 0
    max_gird = None
    for y in range(len(data)):
        for x in [0, -1]:
            direction = Direction.R if x==0 else Direction.L
            grid, count = part_1(data, x, y, direction)
            if count > maximum:
                maximum = count; max_gird = grid

    for x in range(len(data[0])):
        for y in [0, -1]:
            direction = Direction.D if y==0 else Direction.U
            grid, count = part_1(data, x, y, direction)
            if count > maximum:
                maximum = count; max_gird = grid
    return maximum

if __name__ == '__main__':

    _, part_1_ans = part_1(read_data())
    print("Part 1 answer =>", part_1_ans)

    part_2_ans = part_2(read_data())
    print("Part 2 answer =>", part_2_ans)