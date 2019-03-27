def add(a, b):
	"""add(a, b) adds a number 'a' to another number 'b'."""
	return a+b

def subtract(a, b):
	"""subtract(a, b) subtracts a number 'a' from another number 'b'."""
	return a-b

def math(a, b, fnc = add):		# Parameters can be anything (a list, a dictionary, a function, etc)
	return fnc(a, b)

# def speak(animal="dog"):
    
#     if animal == "dog":
#         return "woof"
#     elif animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     return "?"

# Compact answer
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '???')	# The string "???" is passed as a default value in case there's no key matched.

print( math(20,7) )
print( math(20,7, subtract) )

# KEYWORD ARGUMENTS
print( math(fnc=subtract,b=7,a=20) )	# Works the same way to the above.

print(speak())
print(speak("pig"))
print(speak("lion"))

total = 0

def increment():
	# When a variable is defined out of the scope of the function you have to use 
	# the keyword "global" if you intend to change/add the value of that variable
	global total
	total += 2
	return total

print(increment())	# 2

name = "James"
def full_name():
	# If you wanna just use the variable and change anything on it, 
	# you don't need to use the "global" keyword.
	return "Lebron " + name

print(full_name())

name = "James"
def full_name():
	# It works because its overwritting the global variable.
	name = "Lebron James"
	return name

print(full_name())

def outer():
	count = 0
	def inner():
		nonlocal count	# The "nonlocal" keyword let us modify a parent's variable in a child (AKA nested) function.
		count += 3
		return count
	return inner()