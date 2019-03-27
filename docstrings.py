def add(a, b):
	"""add(a, b) adds a number 'a' to another number 'b'."""
	return a+b

def subtract(a, b):
	"""subtract(a, b) subtracts a number 'a' from another number 'b'."""
	return a-b

print( add(20, 5) )
print( subtract(2, 20) )

print(subtract.__doc__)
print(add.__doc__)