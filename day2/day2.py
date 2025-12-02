def readInput(path):
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        return line.split(",")

def check_interval(interval):
    endpoints = interval.split("-")
    begin = int(endpoints[0])
    end = int(endpoints[1])
    counter = 0
    for id in range(begin, end+1):
        if check_id(str(id)):
            counter += id
    return counter

def check_id(id):
    if len(id) & 1 == 1:
        return
    return id[:len(id)//2] == id[len(id)//2:]

def check_id2(id):
    """This assumes a different definition of invalid IDs (sequence can repeate any times)
    well, what do you know, I accidentally solved part 2
    """
    for sub_length in range(1, len(id) // 2 + 1):
        if len(id) % sub_length != 0:
            continue
        if id.replace(id[:sub_length], "") == "":
            return True
    return False

def run():
    intervals = readInput("day2/day2_2.txt")
    counter = 0
    for interval in intervals:
        counter += check_interval(interval)
    print(counter)

run()