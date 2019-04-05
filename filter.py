
nums = range(0,21)

odds = filter( lambda num : num % 2 != 0, nums)
# print(odds)
# print(list(odds))

users = [ 
  	{ "user_name" : "MChammer", "shopcart" : ["HeadPhone Beats", "Mouse Microsoft"]},
  	{ "user_name" : "Paul_George", "shopcart" : ["Basket Ball NIKE", "T-shirt 76ers"]},
  	{ "user_name" : "KittyKat", "shopcart" : []},
  	{ "user_name" : "Rainbow_Killer", "shopcart" : ["Pro Bow", "Silver Arrows"]},
  	{ "user_name" : "GodsSlayer", "shopcart" : []},
  	{ "user_name" : "T'chala", "shopcart" : []},
  	{ "user_name" : "Sam", "shopcart" : []}
]

# Using filters.
empty_shopcarts = list( filter( lambda user : not user["shopcart"], users) )
# print(empty_shopcarts)

# Using List Comprehension.
empty_shopcarts2 = [user["user_name"].upper() for user in users if not user["shopcart"] ]
# print(empty_shopcarts2)

# Using Maps combined w/ Filters.
short_names = list( map( lambda user : user["user_name"].upper(), filter( lambda user : not user["shopcart"], users ) ) )
# print(short_names)

# ----------------------- EXERCISE ------------------------------
def remove_negatives(numbers):
    return list( filter( lambda num : num >= 0, numbers) )

print( remove_negatives([-1,3,4,-99]) )	# [3,4] 
print(remove_negatives([-12,-1,0,24,-58,45,77,32]) )		# [0,24,45,77,32]