def read_input(path):
    matrix = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            matrix.append(list(line))
    return matrix

def count_neighbors(matrix, row, col):
    n = len(matrix)
    m = len(matrix[0])
    counter = 0
    cells_to_check = [(i,j) for i in range(row-1, row + 2) for j in range(col-1, col + 2) if i >= 0 and i < n and j >= 0 and j < m and not(i == row and j == col)]
    for i, j in cells_to_check:
        if matrix[i][j] == "@":
            counter += 1
    return counter

def count_accessable(matrix):
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@" and count_neighbors(matrix, i, j) < 4:
                counter += 1
    return counter

def count_accessable_part2(matrix):
    counter = 0
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == "@" and count_neighbors(matrix, i, j) < 4:
                counter += 1
                matrix[i][j] = "."
                i = max(0, i - 2) # Does not work with -1, not sure why
                j = max(0, j - 2)
            j += 1
        i += 1
    return counter

matrix = read_input("day4/day4_2.txt")
print(count_accessable_part2(matrix))
for row in matrix:
    print("".join(row))



# WRONG:
# 8252