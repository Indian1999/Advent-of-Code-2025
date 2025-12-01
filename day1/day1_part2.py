from math import fabs

def move_dial(dial, value):
    new_dial = dial+value
    if value > 0:
        clicks = fabs(new_dial//100 - dial // 100)
    else:
        clicks = fabs((new_dial-1)//100 - dial // 100)

    if dial % 100 == 0 and value < 0:
        clicks -= 1
    return (new_dial, clicks)

with open("day1/day1_1.txt") as f:
    counter = 0
    dial = 50    
    for line in f:
        line = line.strip()
        value = int(line[1:])
        if line[0] == "L":
            value *= -1
        dial, clicks = move_dial(dial, value)
        counter += clicks
        print(dial, counter)
    print(counter)
        
#Wrong answers:
# 5874
# 5987
# 5984
#Correct: 5978