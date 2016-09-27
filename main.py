#!/usr/bin/python3
import sys

# get the line number with the game no
gameNoString = "#Game No :"

#plik = open(sys.argv[1], "r")
#plik = open("./888poker.txt", "r")
#
#for line in plik:
#    line = line.rstrip()
#    if gameNoString in line:
#        print(lineself.)

lookup = gameNoString

#with open(sys.argv[1]) as myFile:
numeryGier = dict()
counter = 0
with open("./888poker.txt") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            #print( 'found at line:', num)
            numeryGier[counter] = line
            counter += 1

print(numeryGier)
