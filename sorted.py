
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
  	{ "user_name" : "MChammer", "shopcart" : ["HeadPhone Beats", "Mouse Microsoft"]},
  	{ "user_name" : "Paul_George", "shopcart" : ["Basket Ball NIKE", "T-shirt 76ers"]},
  	{ "user_name" : "KittyKat", "shopcart" : []},
  	{ "user_name" : "Rainbow_Killer", "shopcart" : ["Pro Bow", "Silver Arrows"]},
  	{ "user_name" : "GodsSlayer", "shopcart" : []},
  	{ "user_name" : "T'chala", "shopcart" : []},
  	{ "user_name" : "Sam", "shopcart" : []}
]

users = sorted( users, key=lambda user: user["shopcart"] )	# It isn't working properly.
print(users)