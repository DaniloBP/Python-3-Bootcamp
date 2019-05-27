
class Deck(object):

	suits = ["Hearts", "Diamonds", "Clubs" or "Spades"]
	values = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self):
	
		self.total_cards = 0
		
		# new_dict = { value : suit for value in Deck.values and suit in Deck.suits }
		# print(new_dict)

	def count(self):
		return self.total_cards	

deck = Deck()