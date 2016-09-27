#!/usr/bin/python3
import sys

plik = open(sys.argv[0], "r")

for line in plik:
    line = line.rstrip()
    print(line)
