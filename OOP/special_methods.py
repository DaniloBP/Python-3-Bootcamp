class Human:

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age	

	def __repr__(self):
		return f"Human named {self.first} {self.last}"

	def __len__(self):
		return self._age

	def __add__(self, partner):
		if isinstance(partner, Human):
			return Human(first="'Newborn'", last= self.last, age=0)
		raise TypeError("You can't add this 'thing' to a Human.")

	
person = Human("Paloma", "Sullivan", 21)
partner = Human("George", "Ras", 24)
p = 25
print(person)
print(len(person))
# print(person + partner)
# print(person + p)		# raises an error