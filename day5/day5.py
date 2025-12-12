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
    
    def union_of_intervals(self, a, b):
        if a[0] >= b[0] and a[1] <= b[1]:
            return b
        if b[0] >= a[0] and b[1] <= a[1]:
            return a
        if a[0] >= b[0] and a[0] <= b[1] and a[1] >= b[1]:
            return (b[0], a[1])
        if b[0] >= a[0] and b[0] <= a[1] and b[1] >= a[1]:
            return (a[0], b[1])
        return False
        
        

    def count_number_of_fresh_ids(self):
        i = 0
        while i < len(self.ranges):
            j = i + 1
            while j < len(self.ranges):
                union = self.union_of_intervals(self.ranges[i], self.ranges[j])
                if union:
                    self.ranges[i] = union
                    del self.ranges[j]
                    j = i + 1
                else:
                    j += 1
            i += 1
        counter = 0
        for interval in self.ranges:
            counter += interval[1] - interval[0] + 1
        return counter

    
path = os.path.join(os.path.dirname(__file__), "day5_2.txt")
fdb = FoodDatabase(path)
print(fdb.count_fresh())
print(fdb.count_number_of_fresh_ids())


# Wrong answers (part 2):
# 557297295790321
# Correct: 339668510830757