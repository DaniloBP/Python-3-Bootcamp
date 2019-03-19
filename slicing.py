
# list[start:end:step]  (Just like works with 'ranges'.)

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

slice2 = squares[0:-4]		# It doesn't include the last 4 elements.
print(slice2)

slice2 = squares[0:7:3]		# It goes from the first index all the way to the 6th(= 7-1) index stepping 3 by 3 indexes.
print(slice2)

slice2 = squares[3::-1]		# With negative step number it reverses the order. It starts at the third index and 
print(slice2)				# goes backwards to index 0. --> output = [16,9,4,1]

slice2 = squares[:2:-1]		# It starts at the last index and goes backwards to index 3(= 2 + 1). --> output = [100,81,64,49,36,25,16]
print(slice2)				

phrase = "Hi, there!"
rev_phrase = phrase[::-1]	# It reverses lists/strings 
print(rev_phrase)
slice2 = squares[::-1]		# 
print(slice2)

squares[1:5] = ['A','B','C','D','E','F'] 	# Modifies the indexes 1 to 4 in original list and replaces with the list passed.
print(squares)								# Output --> [1,'A','B','C','D','E','F',36,49,64,81,100]

names = ["Mike", "Lucas", "Dustin", "Will", "Eleven", "Max"]
print(names)
names[0], names[1] = names[1], names[0]		# Swaps the positions of the two values.
names[1], names[2] = names[2], names[1]		# Swaps the positions of the two values.
print(names)