#!/usr/bin/python
from sys import argv
from os.path import exists

script_name, from_file, to_file = argv

# we could do these two on one line, how?
indata = open(from_file).read() 

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
