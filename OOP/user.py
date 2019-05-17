
class User(object):
	"""docstring for User"""
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Malcolm", "Batista", 25)
user2 = User("Joe", "Rogan", 174)

# print(user1.first + " " + user1.last + " is " + str(user1.age) + " years old")
# print(user2.first + " " + user2.last + " is " + str(user2.age) + " years old")

print(user1.first, user1.last)
print(user2.first, user2.last)