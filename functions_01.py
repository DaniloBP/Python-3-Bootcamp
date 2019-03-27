from random import random  # use randint(a, b) to generate a random number between a and b

def flip_coin():

	if random() > 0.5:
		return "HEADS"
	else:
		return "TAILS"

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    return [ even for even in range(1,50) if even % 2 == 0 ]

# ------------------------------------------------------------

i = 0  # i should be incremented by one each iteration
while i < 10:    
    print(f" -----\n {flip_coin()}\n -----")
    i += 1

print(f"\n{generate_evens()}\n")