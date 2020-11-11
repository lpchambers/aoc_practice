#!/bin/python3

def isnice(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    
    vowels = sum(s.count(v) for v in 'aeiou')
    if vowels < 3:
        return False

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            break
    else:
        return False

    return True

print(isnice("ugknbfddgicrmopn"))
print(isnice("aaa"))
print(isnice("jchzalrnumimnmhp"))

with open('input') as f:
    lines = f.readlines()

print(sum([isnice(l) for l in lines]))

