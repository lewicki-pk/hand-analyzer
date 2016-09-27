## 2016-09-27

Starting of the project.

Class Player has
* position and related seat
* bankroll
* cards (2 cards or unknown)
* bets (this is only tricky part)


Class Game has
* players
* blinds
* phase (pre-flop, flop, turn, river)

Class HistoryParser
* creates a players
* gets the game flow from the text file
