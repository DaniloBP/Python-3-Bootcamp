# GUESSING GAME WITH ERROR HANDLING
import random


guess = None
random_num = random.randint(1, 11)

while True:	
	try:
		guess = int( input("Enter your guess ( between 1 and 10):\t") )
	except ValueError:
		print("That's not a number.")
	else:
		if guess == random_num:
			print("GOOD JOB, YOU GESSED IT.")
			break
		elif guess > random_num:
			print("Try a LOWER number.")
		elif guess < random_num:
			print("Try a HIGHER number.")
	finally:
		print("RUNS NO MATTER WHAT!")

print("Shutting down...")