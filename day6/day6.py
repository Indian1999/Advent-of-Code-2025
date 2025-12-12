import os
class Math:
    def __init__(self, path):
        self.matrix = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                while "  " in line:
                    line = line.replace("  ", " ")
                line = line.split(" ")
                line = [int(item) if item.isdigit() else item for item in line]
                self.matrix.append(line)
    
    def calculate_col(self, index:int) -> int:
        if self.matrix[-1][index] == "*":
            counter = 1
            for i in range(len(self.matrix) - 1):
                counter *= self.matrix[i][index]
        else:
            counter = 0
            for i in range(len(self.matrix) - 1):
                counter += self.matrix[i][index]
        return counter
    
    def sum_of_all_cols(self):
        counter = 0
        for j in range(len(self.matrix[0])):
            counter += self.calculate_col(j)
        return counter
    
path = os.path.join(os.path.dirname(__file__), "day6_2.txt")
math = Math(path)
print(math.sum_of_all_cols())