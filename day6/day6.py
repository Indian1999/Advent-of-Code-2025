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
    
class Math2:
    """Class to solve part 2 of the puzzle"""
    def __init__(self, path):
        self.matrix = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.replace("\n", "")
                self.matrix.append(line)

    def col_num(self, j:int) -> int:
        num_string = ""
        for i in range(len(self.matrix) - 1):
            num_string += self.matrix[i][j]
        num_string = num_string.strip()
        if num_string == "":
            return None
        else:
            return int(num_string)

    def sum_of_all_cols(self):
        total_counter = 0
        counter = 0
        operation = None
        for j in range(len(self.matrix[0])):
            if self.matrix[-1][j] == "*":
                total_counter += counter
                counter = 1
                operation = "*"
                num = self.col_num(j)
                if num:
                    counter *= num
            elif self.matrix[-1][j] == "+":
                total_counter += counter
                counter = 0
                operation = "+"
                num = self.col_num(j)
                if num:
                    counter += num
            elif operation == "+":
                num = self.col_num(j)
                if num:
                    counter += num
            else:
                num = self.col_num(j)
                if num:
                    counter *= num
        total_counter += counter
        return total_counter

path = os.path.join(os.path.dirname(__file__), "day6_2.txt")
#math = Math(path)
#print(math.sum_of_all_cols())
math = Math2(path)
print(math.sum_of_all_cols())