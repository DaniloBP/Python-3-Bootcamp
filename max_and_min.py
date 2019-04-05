
# max() returns the largest item in an iterable or between two elements.
nums = (45,-555,36,95,88)
# print(f"Max value in {nums}: {max(nums)}\n")
# print(f"Min value in {nums}: {min(nums)}\n")

expr = "Nice to meet you."
# print(f"Max value in {expr}: {max(expr)}\n")
# print(f"Min value in {expr}: {min(expr)}\n")

names = ["Tim", "Ariana", "Rachel", "Edris", "Latifa", "Zendaya"]
# print(f"Max value in {names}: 	{max(names)}\n")
# print(f"Min value in {names}: 	{min(names)}\n")

# print(f"The longest name in {names} is { max( names, key= lambda name: len(name) ).upper() }\n")
# print(f"The shortest name in {names} is { min( names, key= lambda name: len(name) ).upper() }\n")

users = [ 
  	{ "username" : "Mchammer", "num_comments" : 14},
  	{ "username" : "Paul_George", "num_comments" : 22},
  	{ "username" : "KittyKat", "num_comments" : 88},
  	{ "username" : "Rainbow_Killer", "num_comments" : 5},
  	{ "username" : "GodsSlayer", "num_comments" : 11},
  	{ "username" : "Tchala", "num_comments" : 154},
  	{ "username" : "Sam", "num_comments" : 566}
]

print(f"The MOST active user is { max( users, key= lambda u: u['num_comments'])['username'].upper() }\n")
print(f"The LEAST active user is { min( users, key= lambda u: u['num_comments'])['username'].upper() }\n")

# ----------- EXERCISE ------------
# Define extremes below:
def extremes(collection):
	return ( min(collection), max(collection) )

print( extremes([1,2,3,4,5]) )	# (1,5)
print( extremes((-11,542,-41,45,78,111)) )	# (-41,542)
print( extremes("alcatraz"))	# ('a', 'z')