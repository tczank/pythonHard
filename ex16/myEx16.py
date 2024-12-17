#!/usr/bin/python

from sys import argv

script, txt_name = argv
prompt = ':->'

txt = open(txt_name)

print(txt.read())


