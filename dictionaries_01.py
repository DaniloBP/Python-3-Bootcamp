
person = { "first_name" : "Joel", "last_name" : "Embid", "height" : 2.15}
#print(person)

person2 = dict(first_name = "Ben",last_name = "Simmons", height = 2.10)
#print( f"First Name = {person2['first_name']}\nLast Name = {person2['last_name']}\nHeigth = {person2['height']} metros" )

# for value in person.keys():
# 	print(value)

# for value in person.values():
# 	print(value)

for key,value in person.items():		# .items() returns both the keys and the values of some dictionary.
	print(f"{key.upper()} = {value}")