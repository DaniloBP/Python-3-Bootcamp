
player1 = input("\nPlayer 1, choose your option:\n\n"
					+ "\t1 - ROCK\n"
					+ "\t2 - PAPER\n"
					+ "\t3 - SCISSORS\n\n")

if player1:
	if player1 == "1":
		player1 = "ROCK"
	elif player1 == "2":
		player1 = "PAPER"
	elif player1 == "3":
		player1 = "SCISSORS"
	else:
		print("\nInvalid Option!  Choose a valid option.\n")

player2 = input("\nPlayer 2, choose your option:\n\n"
					+ "\t1 - ROCK\n"
					+ "\t2 - PAPER\n"
					+ "\t3 - SCISSORS\n\n")

if player2:
	if player2 == "1":
		player2 = "ROCK"
	elif player2 == "2":
		player2 = "PAPER"
	elif player2 == "3":
		player2 = "SCISSORS"
	else:
		print("\nInvalid Option!  Choose a valid option.\n")

print(f"\nPlayer 1 chose: {player1}\n")
print(f"\nPlayer 2 chose: {player2}\n")

if (player1 == "ROCK" and player2 == "SCISSORS") or (player1 == "PAPER" and player2 == "ROCK") or (player1 == "SCISSORS" and player2 == "PAPER"):
	print("\n\t ---> PLAYER 1 is the WINNER!!\n")
elif (player2 == "ROCK" and player1 == "SCISSORS") or (player2 == "PAPER" and player1 == "ROCK") or (player2 == "SCISSORS" and player1 == "PAPER"):
	print("\n\t ---> PLAYER 2 is the WINNER!!\n")
else:
	print("\n\t --->> It's a TIE! NOBODY wan!\n")
