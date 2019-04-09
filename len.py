
# len() returns the length of an object. The argument may be a sequence (such as string, tuple, list or range)
# or a collection (sucha as a dictionary or set).

users = [ 
  	{ "username" : "Mchammer", "shopcart" : ["HeadPhone Beats", "Mouse Microsoft"]},
  	{ "username" : "Paul_George", "shopcart" : ["Basket Ball NIKE", "T-shirt 76ers"]},
  	{ "username" : "KittyKat", "shopcart" : []},
  	{ "username" : "Rainbow_Killer", "shopcart" : ["Pro Bow", "Silver Arrows"]},
  	{ "username" : "GodsSlayer", "shopcart" : []},
  	{ "username" : "Tchala", "shopcart" : []},
  	{ "username" : "Sam", "shopcart" : []}
]

print(len(users))	# 7
print(len(users[0]))	# 2

# In fact behinds the scenes len() is calling the function .__len__() presents in ""every?"" object.