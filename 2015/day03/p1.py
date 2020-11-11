#!/bin/python3
U = "^"
D = "v"
L = "<"
R = ">"

m = {
    U: (0, -1),
    D: (0, 1),
    L: (-1, 0),
    R: (1, 0),
}

x = 0
y = 0

visited = {(0, 0)}

with open('input') as f:
    l = f.read()

for d in l:
    dx, dy = m.get(d, (0, 0))
    x += dx
    y += dy
    visited.add((x, y))

print(len(visited))
