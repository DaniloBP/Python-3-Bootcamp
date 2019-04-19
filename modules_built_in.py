# import random as rand 	# We can alias a module name too.
# import random
# from random import choice, shuffle, randint
from random import choice as escolher, shuffle as misturar, randint

fruits = ["Apple", "Orange", "Banana", "Watermeloon", "Strawberry"]

# print( random.choice(fruits) )
# print( rand.choice(fruits) )
# print( choice(fruits) )
# print( escolher(fruits) )

# random.shuffle(fruits)
# rand.shuffle(fruits)
# shuffle(fruits)
# misturar(fruits)

# print( random.choice(fruits) )
# print( rand.choice(fruits) )
# print( choice(fruits) )
# print( escolher(fruits) )


# ------------------ EXERCISES -------------------
# 1)
import math

# Use math.sqrt  to find the square root of 15129 and save it to variable called answer:
answer = math.sqrt(15129)
print(answer)

# 2)
import keyword

def contains_keyword(*args):

	for word in args:
		if keyword.iskeyword(word):
			return True
	return False

print( contains_keyword("hello", "Mom", "Anchor") )
print( contains_keyword("if", "hdfhghh", "lslslsls", "omg omg omg omg") )
print( contains_keyword("nbnbnbnb", "hdfhghh", "lslslsls", "omg omg omg omg", "lol", "def") )