#!/usr/bin/python

def do_more_things(a, b):
    print("A IS", a, "B IS", b)
    i = 10
    while i > 0:
        do_more_things(a, b)

# calling function
do_more_things("hello", "bubuti")
