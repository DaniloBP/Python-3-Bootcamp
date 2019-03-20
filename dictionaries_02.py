
# DICTIONARIES METHODS
person = { "first_name" : "Joel", "last_name" : "Embid", "height" : 2.15}
person.clear()		# Deletes all data from a dictionary.

person2 = dict(first_name = "Ben",last_name = "Simmons", height = 2.10)
person = person2.copy()		# Makes a copy of a dictionary in other memory address.

print(person2)

# First parameter has to be a iteratable object and second sets the value which 
# will be associated with each value of the first parameter
empty = {}.fromkeys(["Name", "Phone", "Address", "Age"], "Unknown")		# .fromkeys() function is used usually to creates 
print(empty)															# a dictionary with DEFAULT values.

name = person.get("first_name") + " " + person.get("last_name")		# .get() returns the value associated with the given key.
print(name)															#  In case of the there's no such key it returns 'None'.

# removed = empty.pop("Address")		# Removes the object and returns the value associated with the given key.

# removed = empty.popitem()		# Removes a random key and the value(s) associated with it.
# print(removed)
# print(empty)

person3 = { "country" : "Australia"}	# Updates a dictionary with data from another one but don't removes the existing
person3.update(person)					# values in the updated dictionary but if there's equal keys those are overwritten,
print(person3)							# i.e., it only adds or updates values and keys, never deletes them. 