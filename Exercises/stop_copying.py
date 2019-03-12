phrase = input("Hey, How is it going?\n")

while phrase != "stop copying me":
	if phrase:
		phrase = input(phrase + "\n")
	else:
		print("That's how you're gonna answer may question? SAY SOMETHING!")
		phrase = input()

print("UGH, FINE YOU WIN!\n")
