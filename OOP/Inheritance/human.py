
class Human:

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age	

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value <= 0:
			raise ValueError("The age must be a positive number!")
		self._age = value	

person = Human("Ron", "Salmen", 45)
# print(person.get_age())
print(person.age)
person.age = 25
print(person.age)