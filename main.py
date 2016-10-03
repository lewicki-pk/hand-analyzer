#!/usr/bin/python3
import sys
from collections import OrderedDict

class Game(object):
    def __init__(self, startingLine, endingLine):
        self.fStart = startingLine
        self.fEnd = endingLine

    def parseThisGame(self):
        print("TODO implement me")

################## main ##################

gameNoString = "#Game No :"
lookup = gameNoString

#with open(sys.argv[1]) as myFile:
gameNumber = dict()
with open("./888poker-many-hands.txt") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            gameNumber[num] = line

odGameNumber = OrderedDict(sorted(gameNumber.items()))
gamesList = list()
previous = None
for each in odGameNumber:
    current = each
    if ((previous != None) and (current != None)):
        someGame = Game(previous, current - 1)
        gamesList.append(someGame)
    previous = each

gamesList.append(Game(previous, num))
for eachGame in gamesList:
    print("Game starts in " + str(eachGame.fStart) + " and ends in " + str(eachGame.fEnd) + " line.")

################## sample 888 poker hand history ##################

##Game No : 510750902
#***** 888poker Hand History for Game 510750902 *****
#1/2 Blinds No Limit Holdem - *** 19 09 2016 23:58:16
#Table Henderson 10 Max (Play Money)
#Seat 4 is the button
#Total number of players : 6
#Seat 1: poisonkisses ( 129.70 )
#Seat 2: pikejpeel ( 200 )
#Seat 4: alt0306 ( 26.50 )
#Seat 5: Toka_M. ( 170 )
#Seat 6: lisa1control ( 774.30 )
#Seat 7: marvela14 ( 4,215.17 )
#Toka_M. posts small blind [1]
#lisa1control posts big blind [2]
#pikejpeel posts big blind [2]
#** Dealing down cards **
#Dealt to pikejpeel [ 3h, 7d ]
#marvela14 folds
#poisonkisses folds
#pikejpeel checks
#alt0306 calls [2]
#Toka_M. calls [1]
#lisa1control checks
#** Dealing flop ** [ Tc, Qc, Jd ]
#Toka_M. bets [2]
#lisa1control calls [2]
#pikejpeel folds
#alt0306 raises [4]
#Toka_M. raises [4]
#lisa1control calls [4]
#alt0306 raises [4]
#Toka_M. calls [2]
#lisa1control calls [2]
#** Dealing turn ** [ 4d ]
#Toka_M. checks
#lisa1control checks
#alt0306 checks
#** Dealing river ** [ 8d ]
#Toka_M. bets [32]
#lisa1control calls [32]
#alt0306 calls [16.50]
#** Summary **
#Toka_M. shows [ 2d, Js ]
#lisa1control mucks [ Ah, 7h ]
#alt0306 shows [ Jh, 5s ]
#Toka_M. collected [ 38.75 ]
#alt0306 collected [ 38.75 ]
#Toka_M. collected [ 31 ]
#
