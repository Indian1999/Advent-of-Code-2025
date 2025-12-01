def move_dial(dial, value):
    return (dial + value) % 100

with open("day1/day1_1.txt") as f:
    counter = 0
    dial = 50    
    for line in f:
        line = line.strip()
        value = int(line[1:])
        if line[0] == "L":
            value *= -1
        dial = move_dial(dial, value)
        if dial == 0:
            counter += 1
    print(counter)
        
