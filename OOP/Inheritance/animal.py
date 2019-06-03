
class Animal:

	def __init__(self, name, species):
		self.name = name
		self.species = species

	def make_sound(self, sound):
		raise NotImplementedError("Subclass needs to implement this method!")		

	def __repr__(self):
		return f"{self.name} is a {self.species}"

# -----------------------------------------------------------
class Cat(Animal):

	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat")
		self.breed = breed
		self.toy = toy

	def play(self):
		return f"{self.name} plays with its {self.toy}..."

# ----------------------------------------------------------

kitten = Cat("Green", "Scottish Fold", "String")
print(kitten)
print(kitten.breed)
kitten.make_sound("Meowww")
print(kitten.play())