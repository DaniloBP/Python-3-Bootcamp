# Represents a single Card that must have a SUIT ("Hearts"suits = ["Hearts", "Diamonds", "Clubs" or "Spades"]
# and a value ("A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q" or "K").

class Card:

	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]	

	def __init__(self, suit, value):

		if suit not in Card.suits:
			raise ValueError(f"You can't have '{suit}' as a Suit.")
		if value not in Card.values:
			raise ValueError(f"You can't have {value}' as a Value.")
			
		self.suit = suit
		self.value = value

	def __repr__(self):
		# return f"{self.value} of {self.suit}"
		return self.value + " of " + self.suit