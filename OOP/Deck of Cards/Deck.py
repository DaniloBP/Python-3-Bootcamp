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
		return f"Deck of {self.count()} cards"

	def _deal(self, amount):

		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		elif amount > self.count():
			amount = self.count()
		while amount > 0:
			self.cards.pop()
			self.total_cards -= 1
			amount -= 1

	def deal_card(self):
		self._deal(1)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		elif self.count() == 52:
			shuffle(self.cards) 

	def display_cards(self):
		for card in self.cards:
			print(card)

	def count(self):
		return self.total_cards

deck1 = Deck()
# deck1.display_cards()
print(deck1)
deck1.shuffle()
deck1._deal(6)
deck1.deal_card()
print(deck1.count())
# deck1.shuffle()
# deck1._deal(5)