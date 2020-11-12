#!/bin/python3

with open('input') as f:
    lines = f.readlines()

lights = [[False for _ in range(1000)] for __ in range(1000)]

for line in lines:
    temp = line.strip().split()
    s1 = temp[-3]
    s2 = temp[-1]
    x1, y1 = s1.split(',')
    x2, y2 = s2.split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    if line.startswith("turn on"):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = True
    elif line.startswith("turn off"):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = False
    elif line.startswith("toggle"):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = not lights[x][y]

print(sum([sum(col) for col in lights]))
