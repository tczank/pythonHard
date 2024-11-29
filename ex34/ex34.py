#!/usr/bin/python

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

from dis import dis

dis('''
i = 0
while i < 6:
    i += 1
''')
