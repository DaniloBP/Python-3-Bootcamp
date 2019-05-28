from card import Card
from deck import Deck
from random import shuffle

card1 = Card("Hearts", "J")
print(card1)	

deck1 = Deck()
print(deck1)
deck1.shuffle()
print(deck1.deal_hand(8))
print(deck1.deal_card())
print(deck1)
# deck1.display_cards()