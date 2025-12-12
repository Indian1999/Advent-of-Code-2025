import os
class FoodDatabase:
    def __init__(self, path):
        self.ranges = []
        self.ids = []
        with open(path, "r", encoding="utf-8") as f:
            reading_ranges = True
            for line in f:
                if line == "\n":
                    reading_ranges = False
                    continue
                if reading_ranges:
                    line = line.strip().split("-")
                    self.ranges.append((int(line[0]), int(line[1])))
                else:
                    line = line.strip()
                    self.ids.append(int(line))

    def id_in_any_range(self, id: int) -> bool:
        for lower, upper in self.ranges:
            if id >= lower and id <= upper:
                return True
        return False
    
    def count_fresh(self):
        counter = 0
        for id in self.ids:
            if self.id_in_any_range(id):
                counter += 1
        return counter
    
path = os.path.join(os.path.dirname(__file__), "day5_2.txt")
fdb = FoodDatabase(path)
print(fdb.count_fresh())
