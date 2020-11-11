#!/bin/python3
with open('input') as f:
    lines = f.readlines()

dims = []
for l in lines:
    a, b, c = l.split('x')
    dims.append((int(a), int(b), int(c)))


rib = 0
for a, b, c in dims:
    s = sorted((a,b,c))
    rib += 2 * (s[0] + s[1]) + (a * b * c)

print(rib)
