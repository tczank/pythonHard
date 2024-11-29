#!/usr/bin/python


numbers = []

def printWhile(i):
    if i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return i

i = 0

i = printWhile(i)
i = printWhile(i)
i = printWhile(i)
i = printWhile(i)
i = printWhile(i)
i = printWhile(i)
