
# print( abs(-58))	# 58
# print( abs(22))	# 22

ints = [1,2,3,4]
# ---> sum( collection, start(optional) )
# ---> start = the sum will initiate with this given number.
# print( sum(ints) )	# 10	

# print( sum(ints,5) )	# 5(start) + 10 = 15	
# print( sum([6.1, 6.2, 6.3, 6.4], 2.1) )	# 2.1(start) + (6.1 + 6.2 + 6.3 + 6.4) = 2.1 + 25.0 = 27.1

# round(number, num digits precision), if the second argument is not passed (or 'None' is passed) it's gonna return the nearest integer.
# print( round(2.45) )	# 2
# print( round(2.51) )	# 3
# print( round(2.45456, 2) )	# 2.45
# print( round(64.78998, 4) )	# 64.79
# print( round(7.4542, 3) )	# 7.454

# -------- EXERCISE ---------
def max_magnitude(collection):
	i = 0
	while i < len(collection):
		collection[i] = abs(collection[i])
		i += 1
	return max(collection)
	#     return max(abs(num) for num in nums)		# Works too.

print( max_magnitude([200,300,-999]) )	# 999
print( max_magnitude([-22,-54,-2]) )	# 54