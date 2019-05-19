# A User Class with both class Attributes and class Methods.
class User(object):
	# A class attribute
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users."

	@classmethod
	def from_string(cls, str_data):
		first, last, age = str_data.split(",")
		return cls(first, last, int(age))	

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1		# Every time a new instance is created a user is added to the variable.

	# Class' string representation 
	def __repr__(self):
		return f"\nFirst Name: {self.first}\nLast Name: {self.last}\nAge: {self.age}\n"

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out..."

	def full_name(self):
		return f"{self.first} {self.last}"
		
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

person =  User.from_string("Cathy,Allen,39")
print(person.full_name())
print(person.birthday())
print(person)