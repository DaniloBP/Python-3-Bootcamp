evens = [2,4,6,8,10,12,14,16,18,20]

squares = [1,4,9,16,25,36,49,64,81,100]

# evens[:]	# It gets all the original list.

slice1 = evens[3:]
print(slice1)

slice1 = evens[-4:]
print(slice1)

slice2 = squares[:4]		# It doesn't include the last index, '4' in this specific case.
print(slice2)

slice2 = squares[1:5]		# 
print(slice2)

slice2 = squares[0:-4]		# 
print(slice2)