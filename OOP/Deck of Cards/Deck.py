from card import Card
from random import shuffle

class Deck:

	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self):	
		self.cards = [ Card(suit, value) for suit in Deck.suits for value in Deck.values ]

	def __repr__(self):
		# return f"Deck of {self.count()} cards"
		return "Deck of {} cards".format(self.count())

	def _deal(self, num = 1):
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		# Gets the minimum between the hand and the number of remaining cards  in the deck.
		num = min(self.count(), num)

		hand = self.cards[-num:]
		self.cards = self.cards[:-num]
		return hand

	def deal_card(self):
		# Returns the first element of an one-element list.
		return self._deal()[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
				
		shuffle(self.cards) 
		return self

	def display_cards(self):
		num = 0
		for card in self.cards:
			print(f"{num+1} - {card}")
			num += 1

	def count(self):
		return len(self.cards)