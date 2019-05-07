from pyfiglet import figlet_format
from termcolor import colored

# help(pyfiglet.figlet_format)

# color = ""
# while color != "quit":
# 	text = input("Type in any text:\t")
# 	while True:	
# 		color = input("Type in any of these colors " + 
# 				"(RED, CYAN, GREEN, YELLOW, MAGENTA, WHITE):\t").lower()
# 		try:
# 			ascii_text = 	figlet_format(text)
# 			ascii_colored = colored(ascii_text, color=color)
# 		except KeyError:
# 			if color != "quit":
# 				print("That's not a valid color.")
# 		else:		
# 			print(ascii_colored)
# 			break
# 		finally:
# 			if color == "quit":
# 				print("Shutting down ...")
# 				break


valid_colors = ("red", "cyan", "green", "yellow", "magenta", "white", "blue")
text = input("Type in any text:\t")
color = input("Type in any of these colors " + 
				"(RED, CYAN, GREEN, YELLOW, MAGENTA, WHITE, BLUE):\t").lower()

if color in valid_colors:
	ascii_text = figlet_format(text)
	ascii_colored = colored(ascii_text, color=color)
else:
	color = "yellow"
	ascii_text = figlet_format(text)
	ascii_colored = colored(ascii_text, color=color)

print(ascii_colored)