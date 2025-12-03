def readinput(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def max_in_num_string(numString: str, lower, upper) -> int:
    maxi = lower
    for i in range(lower + 1, upper):
        if int(numString[i]) > int(numString[maxi]):
            maxi = i
    return maxi

def find_max_joltage(numString, n = 12):
    print(numString, end=" -> ")
    indeces = []
    index = 0
    for i in range(1, n+1):
        index = max_in_num_string(numString, index, len(numString) - n + i)
        indeces.append(index)
        index += 1
    result = ""
    for i in indeces:
        result += numString[i]
    print(result)
    return int(result)

if __name__ == "__main__":
    data = readinput("day3/day3_2.txt")
    total = 0
    for line in data:
        total += find_max_joltage(line)
    print(total)
        