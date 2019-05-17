
class User(object):

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def is_senior(self):
		return	self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

user1 = User("Malcolm", "Batista", 25)
user2 = User("Joe", "Rogan", 174)

print(user1.full_name())
print(user2.first, user2.last)
print(f"{user2.full_name()} is a senior?  {user2.is_senior()}.")

print(user2.age)
print(user1.likes("Tapioca"))
print(user2.birthday())