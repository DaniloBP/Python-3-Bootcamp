
people = ["Catherine", "Chelsea", "Carlos", "Caim"]

booleans = [name[0] == 'C' for name in people]
# print(booleans)		# [True,True,True,True]

# Returns True if all elements in the iterable are truthies. Returns True if empty.
# print( all(booleans))	# True

people.append("Dan")
# print( all(name[0] == 'C' for name in people) )	# False

# Returns True if at least one element in the iterable is truthy. Returns False if empty.
# print( any(name[0] == 'C' for name in people))	# True

# print( "<< " + people.pop() + " >>")

# print( [name[0] == 'C' for name in people] )
# print( any(name[0] == 'C' for name in people))	# True
 
# print([name[0] == 'E' for name in people])	# [False, False, False, False]
# print( any([name[0] == 'E' for name in people]) )	# False

# --------------------- EXERCISE -------------------------
# Implement your is_all_strings function below:
def is_all_strings(collection):
    return all( type(elem) == str for elem in collection )

print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings(['a', 'b', 'c', 5]))
print(is_all_strings(["hello", "love", "beauty", "ghdngvjkdvhv khhjjfjf 11232323"]))