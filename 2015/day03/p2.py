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
rx = 0
ry = 0

visited = {(0, 0)}

with open('input') as f:
    l = f.read()


# l = "^v"
# l = "^>v<"
# l = "^v^v^v^v^v"

santa = True
for d in l:
    dx, dy = m.get(d, (0, 0))
    if santa:
        x += dx
        y += dy
        visited.add((x, y))
    else:
        rx += dx
        ry += dy
        visited.add((rx, ry))
    santa = not santa

print(len(visited))
