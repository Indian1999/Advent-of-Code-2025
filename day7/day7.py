import os
from functools import cache

class Manifold:
    def __init__(self, path):
        self.matrix = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                self.matrix.append(list(line))
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])

    def find_start(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == "S":
                    return (i,j)
        raise Exception("Starting position not found!")
    
    def calculate_splits(self):
        """solves part 2"""
        i, j = self.find_start()
        splits = self.move_beam(i, j)
        return splits
    
    @cache
    def move_beam(self, i, j):
        if i >= self.n or j < 0 or j >= self.m:
            return 0
        if self.matrix[i][j] == "^":
            #self.matrix[i][j] = "." # To avoid double counts (good for part 2 maybe? yes)
            return 1 + self.move_beam(i, j-1) + self.move_beam(i, j+1)
        print(i, j)
        return self.move_beam(i+1, j)
    
    def count_char(self, char):
        counter = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == char:
                    counter += 1
        return counter
    
    def print_matrix(self):
        with open(os.path.join(os.path.dirname(__file__), "output.txt"), "w", encoding="utf-8") as f:
            for i in range(self.n):
                for j in range(self.m):
                    f.write(self.matrix[i][j])
                f.write("\n")

    def will_it_split(self, i, j):
        if self.matrix[i][j] == "." or self.matrix[i][j] == "S":
            return False
        row = i - 1
        while row >= 0:
            if self.matrix[row][j] == "^":
                return False
            if self.matrix[row][j] == "S":
                return True
            if (j < self.m and self.matrix[row][j+1] == "^") or (j > 0 and self.matrix[row][j-1] == "^"):
                return True
            row -= 1
        return False
    
    def calculate_splits_2(self):
        """solves part 1"""
        counter = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.will_it_split(i, j):
                    counter += 1
        return counter

path = os.path.join(os.path.dirname(__file__), "day7_2.txt")
manifold = Manifold(path)
print(manifold.calculate_splits() + 1)
#manifold.print_matrix()
#print(manifold.count_char("#"))

# WRONG answers:
# part1:
#   1751
# correct: 1651

# part2: correct: 108924003331749