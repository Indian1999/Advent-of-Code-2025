import os
from math import fabs

PATH = os.path.join(os.path.dirname(__file__), "day9_2.txt")
data = []

with open(PATH) as f:
    for line in f:
        line = line.strip().split(",")
        data.append((int(line[0]), int(line[1])))

def rect_area(a, b):
    return round((fabs(a[0] - b[0]) + 1) * (fabs(a[1] - b[1])+1))

def find_largest_rect(data):
    max = 0
    for i in range(len(data)-1):
        for j in range(i + 1, len(data)):
            area = rect_area(data[i], data[j])
            #print(area, data[i], data[j])
            if area > max:
                max = area
    return max

print(find_largest_rect(data))


