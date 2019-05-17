
# A User Class with both class Attributes and class Methods.
class User(object):

	# A class attribute
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1		# Every time a new instance is created a user is added to the variable.

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out..."

	def full_name(self):
		return f"{self.first} {self.last}"

	def is_senior(self):
		return	self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

print(User.active_users)
user1 = User("Kayle", "Smith", 21)
user2 = User("Jonathan", "Rufus", 34)
print(User.active_users)
print(user1.logout())
print(User.active_users)