#!/bin/python3
with open('input') as f:
    lines = f.readlines()

sig_rep = {}
for line in lines:
    bef, aft = line.strip().split('->')
    sig_rep[aft.strip()] = bef.strip()

sig_val = {}

def find(sig):
    try:
        res = int(sig)
        sig_val[sig] = res
        return res
    except:
        pass

    if sig in sig_val:
        return sig_val[sig]

    rep = sig_rep[sig]

    args = rep.split()
    if 'AND' in rep:
        a1, _, a2 = args
        v1 = find(a1)
        v2 = find(a2)
        res = v1 & v2
    elif 'OR' in rep:
        a1, _, a2 = args
        v1 = find(a1)
        v2 = find(a2)
        res = v1 | v2
    elif 'NOT' in rep:
        _, a1 = args
        v1 = find(a1)
        res = 0xffff - v1
    elif 'LSHIFT' in rep:
        a1, _, ls = args
        res = find(a1) << int(ls)
    elif 'RSHIFT' in rep:
        a1, _, rs = args
        v1 = find(a1)
        res = v1 >> int(rs)
    else:
        res = find(rep)

    sig_val[sig] = res
    return res

print(find('a'))
