
matrix1 = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
# print(matrix1, end="\n\n")


# print(matrix1[0][1], end="\n\n")		# 2

# print(matrix1[1][-1], end="\n\n")		# 8

# print(matrix1[2][-4], end="\n\n")		# 9

# print(matrix1[-2][-3], end="\n\n")		# 6


# for l in matrix1:
# 	print("  ", end="")
# 	for val in l:
# 		print(val, end="\t")
# 	print()

# [ [ print(val) for val in l] for l in matrix1]	# Using List Comprehension.

# board = [ [ num for num in range(1,4)] for val in range(1,4) ]
# print(board)

# board = [ ['X' if num % 2 != 0 else 'O' for num in range(1,4)] for val in range(1,4) ] 
# print(board)

# board = [ ['*' for num in range(1,4)] for val in range(1,4) ] 
# print(board)

# EXERCISES

answer = [ [ i for i in range(0,5)] for val in range(0,5) ]
print(answer)