from deuces import Card
from deuces import Evaluator

card = Card.new('Qh')
#print(card)

print("1========================================")

board = [
        Card.new('Ah'),
        Card.new('2d'),
        Card.new('3c'),
        Card.new('4c'),
        Card.new('4s')
        ]

hand = [
        Card.new('Qs'),
        Card.new('5h')
        ]

Card.print_pretty_cards(board + hand)

evaluator = Evaluator()
print evaluator.evaluate(board, hand)

print("2========================================")

from deuces import Deck
deck = Deck()
#board = deck.draw(5)
player1_hand = deck.draw(2)
player2_hand = deck.draw(2)

Card.print_pretty_cards(board)
Card.print_pretty_cards(hand)
Card.print_pretty_cards(player2_hand)

print("3========================================")

p1_score = evaluator.evaluate(board, hand)
p2_score = evaluator.evaluate(board, player2_hand)

p1_class = evaluator.get_rank_class(p1_score)
p2_class = evaluator.get_rank_class(p2_score)

print "Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class))
print "Player 2 hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class))

hands = [hand, player2_hand]
evaluator.hand_summary(board, hands)

