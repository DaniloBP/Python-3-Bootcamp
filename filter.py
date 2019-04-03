
nums = range(0,21)

odds = filter( lambda num : num % 2 != 0, nums)
# print(odds)
# print(list(odds))

users = [ 
		  { "user_name" : "MChammer", "shopcart" : ["HeadPhone Beats", "Mouse Microsoft"]},
		  { "user_name" : "Paul_George", "shopcart" : ["Basket Ball NIKE", "T-shirt 76ers"]},
		  { "user_name" : "KittyKat", "shopcart" : []},
		  { "user_name" : "Rainbow_Killer", "shopcart" : ["Pro Bow", "Silver Arrows"]},
		  { "user_name" : "GodsSlayer", "shopcart" : []}
		]

buyers = list( filter( lambda user : not user["shopcart"], users) )
print(buyers)
