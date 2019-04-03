

nums = [1,3,5,7,9]

squares = map(lambda x: x ** 2, nums)		# map() is a standard function which takes at least 2 arguments: a function and a iterable (list, string, tuple,...)
# print(squares)
# for sqr in squares:
#	print(sqr)

# print( list(squares) )

triples = list( map(lambda num: 3 * num, nums) )	# Converting a map into a List (The right way)
# print(triples)

people = [ 	{"first" : "John", "last" : "Oliver"},
			{"first" : "Mark", "last" : "Webber"},
			{"first" : "Connor", "last" : "Kent"},
			{"first" : "Mike", "last" : "Tyson"}   ]

last_uppers = list ( map( lambda name : name["last"].upper(), people) )
print(last_uppers)

# ------------ EXERCISE ---------------
def decrement_list(collection):
    return list( map( lambda num: num-1, collection))

print( decrement_list(nums) )