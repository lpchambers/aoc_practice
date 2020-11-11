#!/bin/python3
with open('input') as f:
    l = f.read()

print(l.count('(') - l.count(')'))
