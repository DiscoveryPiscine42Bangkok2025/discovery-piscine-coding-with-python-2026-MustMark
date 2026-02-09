#!/usr/bin/env python3

age = int(input('Please tell me your age: '))

print(f'You are currently {age} years old.')

for add in range(10, 40, 10):
    print(f"In {add} years, you'll be {age + add} years old.")