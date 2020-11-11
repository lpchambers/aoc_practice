#!/bin/python3
import hashlib

inp = "ckczppom"

def hash(i):
    return hashlib.md5(i.encode()).hexdigest()

i=0
while True:
    if hash(f"{inp}{i}").startswith("000000"):
        print(i)
        break
    i += 1
