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

# EXERCISE
def divide_v2(a, b):
	try:
		return a/b
	except ZeroDivisionError:
		print("Please do not divide by zero")
	except TypeError:
		print("Please provide two integers or floats")

# divide(3,0)
# divide(3,'a')		
# divide(3,15)		

print(divide_v2(4,2))  # 2.0
divide_v2([],"1")  # "Please provide two integers or floats"
divide_v2(1,0)  # "Please do not divide by zero"