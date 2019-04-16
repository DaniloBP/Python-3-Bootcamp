
def colorize(text, color):
	valid_colors = ("red", "green", "purple", "gray", "black")
	if type(text) is not str:
		raise TypeError("The text must be an instance of str!")
	if color not in valid_colors:
		raise ValueError("Invalid color.")
	return (f"The text {text} is {color} now.")

print(colorize("Hello!!", "Blue"))
# print(colorize(33, "Blue"))