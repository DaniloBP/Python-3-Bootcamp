def divide(a, b):
	try:
		result = a/b
#	except (ZeroDivisionError, TypeError) as err:
	except ZeroDivisionError:
		print("You can't divide a number by zero.")
	except TypeError as err:
		print("You must pass ONLY NUMBERS.")
		print(err)
	else:
		print(f" {a} divided by {b} is {result}")

divide(3,0)
divide(3,'a')		
divide(3,15)		