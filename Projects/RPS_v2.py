from random import choice

player1 = input("\nPlayer 1, choose your option:\n\n"
					+ "\t1 - ROCK\n"
					+ "\t2 - PAPER\n"
					+ "\t3 - SCISSORS\n\n")

#print("******* NO CHEATING *******\n" * 10)

cpu = choice(['ROCK','PAPER', 'SCISSORS'])

if player1:
	print("\nCPU choice -->  " + cpu + "\n")
#	print("\nPLAYER 1 choice -->  " + player1 + "\n")

	if player1 == "1" and cpu == "SCISSORS":
		player1 = "ROCK"
		print("\n\t << PLAYER 1 >> is the WINNER!!\n")
	elif player1 == "2" and cpu == "ROCK":
		player1 = "PAPER"
		print("\n\t << PLAYER 1 >> is the WINNER!!\n")
	elif player1 == "3" and cpu == "PAPER":
		player1 = "SCISSORS"
		print("\n\t << PLAYER 1 >> is the WINNER!!\n")
	elif player1 != "1" and player1 != "2" and player1 != "3":
		print("\nInvalid Option!  Choose a valid option.\n")
	else:
		print("\n\t << CPU >> is the WINNER!!\n")

	if (cpu == player1):
		print("\n\t <<< It's a TIE! NOBODY won! >>>\n")

else:
	print("You have to choose an option. Try again.")