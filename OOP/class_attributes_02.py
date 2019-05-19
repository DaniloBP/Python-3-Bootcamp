
# A class Pet that only accept species that are in a specific list as pets. 

class Pet:

	allowed = ["dog", "cat", "fish", "rat"]

	def __init__(self, name, species):
		
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a '{species}' as a pet.")
		self.name = name
		self.species = species

pet1 = Pet("Arn", "cat")
# pet2 = Pet("The G.O.A.T.", "goat")
pet2 = Pet("The G.O.A.T.", "dog")

# They all share the same list 'allowed' as you can see on the prints bellow.
print(id(Pet.allowed))
print(id(pet1.allowed))
print(id(pet2.allowed))