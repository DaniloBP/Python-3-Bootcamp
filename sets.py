# 

numbers = {1,2,6,8,5,3,3,3}		# SETS CAN'T HAVE DUPLICATES!
print(f"{type(numbers)} -- > {numbers}\n")

new_set = set({2,1,5,'b','h',True,24.655})		# It's unclear to me why the boolean value isn't been showed when the set is printed.
print(f"{type(new_set)} -- > {new_set}\n")
print(f"5 in new_set?  {5 in new_set}\n'z' in new_set?  {'z' in new_set}\nTrue in new_set?  {True in new_set}\n")

# new_set = set({False,True, 'g'})	
# print(f"{type(new_set)} -- > {new_set}\n")

#for element in new_set:
#	print(element)


countries = ["Brazil", "Canada", "Germany", "France", "South Africa", "Camaroon", "USA", "Colombia", "USA", "Brazil", "Nigeria", "India", "Ethiopia", "South Africa"]
# print(countries)
# print(len(countries))

# If we convert the List above into a Set we're gonna get a list of unique countries (without  duplicates).
countries = set(countries)
# print(countries)
# print(len(countries))

countries.add("Angola")
countries.add("Japan")
countries.add("Brazil")		# This is not gonna change anything in the set.

print(countries)
print(len(countries))

# countries.remove("Germany")
# countries.remove("Argentina")		# If a invalid value is passed it's gonna throw a KeyError.

# countries.discard("Japan")			# Works like .remove() but don't throw an error in case of invalid value.

# print(countries)
# print(len(countries))

# copy_set = countries.copy()
# copy_set.add("Argentina")
# copy_set.add("Barbados")
# print(copy_set)

# copy_set.clear()		# Clears out the whole set.
# print(copy_set)

# MATH WUTH SETS

first_world = {"USA", "Sweden", "South Korea", "Germany", "England", "Canada", "France"}

union = countries | first_world				# Performs the UNION of the 2 Sets just like in real world Math.
print(union)
print(len(union))

intersection = countries & first_world		# Performs the INTERSECTION of the 2 Sets just like in real world Math.
print(intersection)
print(len(intersection))