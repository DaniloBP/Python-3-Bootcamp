from random import random  # use randint(a, b) to generate a random number between a and b

def flip_coin():

	if random() > 0.5:		# random() generates a Float number between 0.0 and 1.0 (not included)
		return "HEADS"
	else:
		return "TAILS"

#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    return [ even for even in range(1,50) if even % 2 == 0 ]

def square(num):
	return num * num

def exponent(num, power=2):
	return num ** power

# Using the string format() method:
# def yell(word):		
#    return "{}!".format(word.upper())
# ------------------------------------------------------------

i = 0
while i < 5:    
    print(f" -----\n {flip_coin()}\n -----")
    i += 1

print(f"\n\n{generate_evens()}\n\n")

num = 13
print(f"The square of {num} is {square(num)}.\n")
# exp = 3
# print(f"The exponantiation of {num} by {exp} is {exponent(num)}.\n")
print(exponent(8))
print(exponent(8,3))