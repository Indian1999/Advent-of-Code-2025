def readinput(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def max_in_num_string(numString: str) -> int:
    maxi = 0
    for i in range(1, len(numString)):
        if int(numString[i]) > int(numString[maxi]):
            maxi = i
    return maxi

def find_max_joltage(numString):
    first = max_in_num_string(numString[:-1])
    second = max_in_num_string(numString[first+1:]) + first + 1
    return int(str(numString[first]) + str(numString[second]))

if __name__ == "__main__":
    data = readinput("day3/day3_2.txt")
    total = 0
    for line in data:
        total += find_max_joltage(line)
    print(total)
        