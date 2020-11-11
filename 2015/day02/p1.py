#!/bin/python3
with open('input') as f:
    lines = f.readlines()

dims = []
for l in lines:
    a, b, c = l.split('x')
    dims.append((int(a), int(b), int(c)))


pap = 0
for a, b, c in dims:
    s = sorted((a,b,c))
    pap += 2 * (a*b + a*c + b*c) + (s[0] * s[1])

print(pap)
