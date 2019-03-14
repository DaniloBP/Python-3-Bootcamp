import random

while True:

	player1 = input("\nPlayer 1, choose your option:\n\n"
						+ "\t1 - ROCK\n"
						+ "\t2 - PAPER\n"
						+ "\t3 - SCISSORS\n\n")

	cpu = random.randint(1, 3)

	if player1:
		print(f"\nCPU choice -->  {cpu}\n")
		player1 = int(player1)

		if (cpu == player1):
			print("\n\t <<< It's a TIE! NOBODY won! >>>\n")
		elif player1 == 1 and cpu == 3:
			cpu = "SCISSORS"
			print("\n\t << PLAYER 1 >> is the WINNER!!\n")
		elif player1 == 2 and cpu == 1:
			cpu = "ROCK"
			print("\n\t << PLAYER 1 >> is the WINNER!!\n")
		elif player1 == 3 and cpu == 2:
			cpu = "PAPER"
			print("\n\t << PLAYER 1 >> is the WINNER!!\n")
		elif player1 != 1 and player1 != 2 and player1 != 3:
			print("\nInvalid Option!  Choose a valid option.\n")
		else:
			print("\n\t << CPU >> is the WINNER!!\n")

		again = input("\nDo you wanna play again? (y/n)\t")
		if again != 'y':
			print("\nThank you for playing!!\nShutting down...\n\n")
			break			
	else:
		print("You have to choose an option. Try again.")