
# try:
# 	# bigfoot
# 	print("Now it's good.")
# except:
# 	print("PROBLEM!!")
# print("After the TRY.")

def get(diction, key):
	try:
		return diction[key]
	except KeyError:
		return None

d = { "name" : "Danny", "city" : "Atlanta"}

print( get(d, "name"))
print( get(d, "age"))
print( get(d, "city"))
