import os
import time
from math import fabs
from pprint import pprint

PATH = os.path.join(os.path.dirname(__file__), "day9_2.txt")
data = []

with open(PATH) as f:
    for line in f:
        line = line.strip().split(",")
        data.append((int(line[0]), int(line[1])))

def rect_area(a, b):
    return round((fabs(a[0] - b[0]) + 1) * (fabs(a[1] - b[1])+1))

def find_largest_rect(data):
    max = 0
    for i in range(len(data)-1):
        for j in range(i + 1, len(data)):
            area = rect_area(data[i], data[j])
            #print(area, data[i], data[j])
            if area > max:
                max = area
    return max

def is_valid(data, a, b):
    a, b = data[a], data[b]
    counter = 0
    from_0, to_0 = min(a[0], b[0]), max(a[0], b[0])
    from_1, to_1 = min(a[1], b[1]), max(a[1], b[1])
    for i in range(from_0, to_0 + 1):
        for j in range(from_1, to_1 + 1):
            if (i,j) in data:
                counter += 1
    print("Validity counter:", counter, a, b)
    return counter == 4


def find_largest_rect_limited(data):
    max = 0
    for i in range(len(data)-1):
        for j in range(i + 1, len(data)):
            if not is_valid(data, i, j):
                continue
            area = rect_area(data[i], data[j])
            if area > max:
                max = area
                print(data[i], data[j])
    return max


def print_tiles(data):
    matrix = [["." for j in range(13)] for i in range(13)]
    for x, y in data:
        matrix[x][y] = "#"
    for row in matrix:
        print(row)

class Floor:
    def __init__(self, data):
        self.red_tiles = data
        self.green_tiles = []
        self.maxX = max(self.red_tiles, key=lambda x: x[0])[0]
        self.maxY = max(self.red_tiles, key=lambda x: x[1])[1]
        for x, y in self.red_tiles:
            found = False
            dx = 1
            while not found:
                if (x + dx, y) in self.red_tiles:
                    self.green_tiles += [(i, y) for i in range(x+1, x + dx)]
                    found = True    
                if (x - dx, y) in self.red_tiles:
                    self.green_tiles += [(i, y) for i in range(x - dx + 1, x)]
                    found = True
                dx += 1
            found = False
            dy = 1
            while not found:
                if (x, y + dy) in self.red_tiles:
                    self.green_tiles += [(x, i) for i in range(y+1, y + dy)]
                    found = True    
                if (x, y - dy) in self.red_tiles:
                    self.green_tiles += [(x, i) for i in range(y - dy + 1, y)]
                    found = True
                dy += 1
        self.edge_tiles = self.red_tiles + self.green_tiles
        self.inner_tiles = []
        # The following part is way too slow, this needs to be rwwritten, takes aprox. 12 hours to complete
        i = 0
        start = time.perf_counter()
        for x, y in self.green_tiles:
            if i % 50 == 0:
                print(f"{i}/{len(self.green_tiles)}")
                print(f"Elapsed time: {time.perf_counter()-start}")
                start = time.perf_counter()
            i+= 1
            if (x-1, y) in self.edge_tiles and (x+1, y) in self.edge_tiles: # Search y
                opposite = self.find_opposite((x, y), axis = 0)
                if opposite[1] > y:
                    self.inner_tiles.append({"fixed_axis": "x", "x": x, "y": (y+1, opposite[1]-1)})
                else:
                    self.inner_tiles.append({"fixed_axis": "x", "x": x, "y": (opposite[1]+1, y-1)})
            if (x, y-1) in self.edge_tiles and (x, y+1) in self.edge_tiles: # Search x
                opposite = self.find_opposite((x, y), axis = 1)
                if opposite[0] > x:
                    self.inner_tiles.append({"fixed_axis": "y", "x": (x+1, opposite[0]-1), "y": y})
                else:
                    self.inner_tiles.append({"fixed_axis": "y", "x": (opposite[0]+1, x-1), "y": y})

    def find_opposite(self, pos, axis):
        for tile in self.edge_tiles:
            if pos != tile and pos[axis] == tile[axis]:
                return tile
    
    def export(self, path = None):
        if path == None:
            path = os.path.join(os.path.dirname(__file__), "floor.txt")
        print("max:", self.maxX, self.maxY)
        lines = [["." for j in range(self.maxY+1)]  for i in range(self.maxX + 1)]
        for x,y in self.red_tiles:
            lines[x][y] = "#"
        for x,y in self.green_tiles:
            lines[x][y] = "O"
        lines = ["".join(line) + "\n" for line in lines]
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    def coord_inside_area(self, pos):
        if pos in self.edge_tiles:
            return True
        for tile in self.inner_tiles:
            if tile["fixed_axis"] == "x" and pos[0] == tile["x"] and pos[1] >= tile["y"][0] and pos[1] <= tile["y"][1]:
                return True
            if tile["fixed_axis"] == "y" and pos[1] == tile["y"] and pos[0] >= tile["x"][0] and pos[0] <= tile["x"][0]:
                return True
        return False


    def rect_area(self, a, b):
        return round((fabs(a[0] - b[0]) + 1) * (fabs(a[1] - b[1])+1))
    
    def is_valid_square(self, a, b):
        from_0, to_0 = min(a[0], b[0]), max(a[0], b[0])
        from_1, to_1 = min(a[1], b[1]), max(a[1], b[1])
        for i in range(from_0, to_0 + 1):
            for j in range(from_1, to_1+1):
                if not self.coord_inside_area((i,j)):
                    return False
        return True
    
    def find_largest_area(self):
        max = 0
        for i in range(len(self.red_tiles)-1):
            for j in range(i+1, len(self.red_tiles)):
                if self.is_valid_square(self.red_tiles[i], self.red_tiles[j]):
                    area = self.rect_area(self.red_tiles[i], self.red_tiles[j])
                    if area > max:
                        print(self.red_tiles[i], self.red_tiles[j])
                        max = area
        return max
            
floor = Floor(data)
#floor.export()
print(floor.find_largest_area())
#for i in range(floor.maxX+1):
#    for j in range(floor.maxY+1):
#        print("#" if floor.coord_inside_area((i,j)) else ".", end="")
#    print()
#pprint(floor.inner_tiles)


