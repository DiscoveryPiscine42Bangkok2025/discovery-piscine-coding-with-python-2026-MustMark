#!/usr/bin/env python3

text = input()

for i in text:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
    
print()