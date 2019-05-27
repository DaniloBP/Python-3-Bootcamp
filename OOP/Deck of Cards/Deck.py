from card import Card
from random import shuffle

class Deck:

	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self):
	
		self.total_cards = 0
		self.cards = []

		for suit in Deck.suits:
			for value in Deck.values:
				self.cards.append( Card(suit, value) )
				self.total_cards += 1

	def __repr__(self):
		# return f"Deck of {self.count()} cards"
		return "Deck of " + str(self.count()) + " cards"

	def _deal(self, amount = 1):
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		elif amount == 1:
			self.total_cards -= 1
			return self.cards.pop(-1)	# Returns a single card from the deck.
		elif amount > self.count():
			amount = self.count()

		popped = []
		while amount > 0:
			popped.append( self.cards.pop() )
			self.total_cards -= 1
			amount -= 1
		return popped

	def deal_card(self):
		return self._deal()

	def deal_hand(self, amount):
		return self._deal(amount)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		elif self.count() == 52:
			shuffle(self.cards) 
			return self.cards

	def display_cards(self):
		num = 0
		for card in self.cards:
			print(f"{num+1} - {card}")
			num += 1

	def count(self):
		return self.total_cards