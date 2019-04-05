
numbers = [5,32,-99,556,-10,1,0]

sorted_nums = sorted(numbers)	# sorted() returns a sorted list. Works with any iterable.

print(numbers)
print(sorted_nums)

numbers.sort()
print(numbers)		# .sort() it's a list specific method and sort the elements in place, i.e., in the same list.

people = ("Jacob", "Ziggy", "Anne","Philip", "Bernides")	# Works w/ Tuples too.
sorted_p = sorted(people)
print(sorted_p)

sorted_nums = sorted(numbers, reverse=True)
print(sorted_nums)

users = [ 
  	{ "username" : "Mchammer", "shopcart" : ["HeadPhone Beats", "Mouse Microsoft"]},
  	{ "username" : "Paul_George", "shopcart" : ["Basket Ball NIKE", "T-shirt 76ers"]},
  	{ "username" : "KittyKat", "shopcart" : []},
  	{ "username" : "Rainbow_Killer", "shopcart" : ["Pro Bow", "Silver Arrows"]},
  	{ "username" : "GodsSlayer", "shopcart" : []},
  	{ "username" : "Tchala", "shopcart" : []},
  	{ "username" : "Sam", "shopcart" : []}
]

# users = sorted( users, key=lambda user: user["username"] )	# Sorts the list of dicts by the "username" key.
users = sorted( users, key=lambda user: len(user["shopcart"]), reverse=True)
print(users)