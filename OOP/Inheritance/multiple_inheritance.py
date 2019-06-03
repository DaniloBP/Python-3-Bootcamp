class Aquatic:

	def __init__(self, name):
		self.name = name

	def swim(self):
		return f"{self.name} is swimming."

	def greet(self):
		return f"Hello, I'm {self.name} and I live in the water."

class Ambulatory:

	def __init__(self, name):
		self.name = name

	def walk(self):
		return f"{self.name} is walking."

	def greet(self):
		return f"Hello, I'm {self.name} and I live on the land."

class Penguin(Aquatic, Ambulatory):

	def __init__(self, name):		
		super().__init__(name=name)


captain = Penguin("Captain")
print(captain.walk())
print(captain.swim())
print(captain.greet())

print(f"Is Captain an instance of Penguin? {isinstance(captain, Penguin)}")
print(f"Is Captain an instance of Aquatic? {isinstance(captain, Aquatic)}")
print(f"Is Captain an instance of Ambulatory? {isinstance(captain, Ambulatory)}")
print(f"Is Captain an instance of Object? {isinstance(captain, object)}")