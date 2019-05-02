from termcolor import colored

# help(termcolor)

#text = colored("Hello, World!!", color="cyan", on_color="on_magenta")
text = colored("HELLO, WORLD!!", color="magenta", on_color="on_green", attrs=["blink"])

print(text)