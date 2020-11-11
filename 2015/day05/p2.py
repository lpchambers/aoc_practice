#!/bin/python3

def isnice(s):
    for i in range(len(s)-2):
        sub = s[i:i+2]
        if s.find(sub, i+2) != -1:
            break
    else:
        return False

    # 1 letter between
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            break
    else:
        return False

    return True

with open('input') as f:
    lines = f.readlines()


print(isnice("qjhvhtzxzqqjkmpb"))
print(isnice("xxyxx"))
print(isnice("uurcxstgmygtbstg"))
print(isnice("ieodomkazucvgmuy"))
print(isnice("aaa"))

tot = 0
for l in lines:
    if isnice(l.strip()):
        tot += 1
        q = 'nice'
    else:
        q = 'naut'
    print(f"{l.strip()} {q} {tot}")

#print(sum([isnice(l.strip()) for l in lines]))

