

nums = [1,3,5,7,9]

squares = map(lambda x: x ** 2, nums)		# map() is a standard function which takes at least 2 arguments: a function and a iterable (list, string, tuple,...)
# print(squares)

triples = list( map(lambda num: 3 * num, nums) )

print(triples)
# print( list(squares) )		# Converting a map into a List.

for sqr in squares:
	print(sqr)

print()
print( list(squares) )		# Converting a map into a List.