#!/usr/bin/python

# import the dis function
from dis import dis

dis('''
x = 10
y = 20
z = x + y
''')

dis('''
while True:
    x = 10
''')

dis("while True: a = 10")

dis('''
x = 0
if x > 0:
    y = 10
''')

dis("input('Yes? ')")
