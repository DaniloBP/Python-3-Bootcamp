import random  # use randint(a, b) to generate a random number between a and b

number = random.randint(1, 20) # store random number in here
guess = None

while True:
	guess = int( input("\nGuess a number between 1 to 20...\n") )

	if guess == number:
		print(f"\nYAY, you guessed it!!\nThe number is << {number} >>\n".upper())
		keep = input("Do you want to keep playing?")
		if keep == 'y':
			number = random.randint(1, 20)
			guess = None
		else:
			print("\nThank you for playing!\n\n")
			break
	elif guess > number:
		print("\nToo HIGH, bitch!\n")
	else:
		print("\nToo LOW, mothafucker!\n")


