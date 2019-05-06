import pyfiglet
from termcolor import colored

# help(pyfiglet.figlet_format)

text = input("Type in any text:\t")
color = input("Type in any of these colors (RED, CYAN, GREEN, YELLOW, MAGENTA, WHITE):\t")

ascii_text = pyfiglet.figlet_format(text)
ascii_colored = colored(ascii_text, color="red")
print(ascii_colored)