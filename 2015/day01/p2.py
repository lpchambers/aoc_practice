#!/bin/python3
with open('input') as f:
    l = f.read()

floor = 0
inst = 0
while floor >= 0:
    inst += 1
    floor += 1 if l[inst-1] == '(' else -1

print(inst)
