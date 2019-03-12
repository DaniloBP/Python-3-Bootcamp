seqc = range(1, 21)

# for num in seqc:
# 	if num == 4 or num == 13:
# 		print(f"\n{num} is UNLUCKY!\n")
# 	elif num % 2 == 0:
# 		print(f"\n{num} is EVEN!\n")
# 	else:
# 		print(f"\n{num} is ODD!\n")

state = ""
for num in seqc:
	if num == 4 or num == 13:
		state = "UNLUCKY"
	elif num % 2 == 0:
		state = "EVEN"
	else:
		state = "ODD"
	
	print(f"\n{num} is {state}!\n")