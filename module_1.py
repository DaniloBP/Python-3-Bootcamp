# SOME FUNCTIONS

def add(*numbers):
	result = 0
	try:
		for num in numbers:
			result += num
	except TypeError as err:
		print("You must pass ONLY NUMBERS.")
		print(err)
	return result

def divide(a, b):
	try:
		result = a/b
	except ZeroDivisionError:
		return "You can't divide a number by zero."
	except TypeError as err:
		return "You must pass ONLY NUMBERS."
	else:
		return result