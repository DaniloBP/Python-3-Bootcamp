
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

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		# This is just for illustration, it isn't a good practice.
		self.first, self.last = name.split(" ")		

	
person = Human("Ron", "Salmen", 45)
# print(person.get_age())
print(person.age)
print(person.full_name)
person.full_name = "Carl Smith"
print(person.full_name)