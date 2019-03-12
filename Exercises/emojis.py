
# rang = range(1, 11)

# UGLY SOLUTION 1
# for current in rang:
# 	for star in range(1, current+1):
# 		print("#", end="")
# 	print("\n")

# ------------------------------
# num1 = 1

# UGLY SOLUTION 2
# while num1 <= 10:
# 	num2 = 0
# 	while num2 < num1:
# 		print("#", end="")
# 		num2 += 1
# 	print("\n")
# 	num1 += 1

# ----------------------------
# rang = range(1, 11)

# for seq in rang:
# 	print("&" * seq)

# ---------------------------
num = 1
print("")
while num <= 10:
	print("$ " * num)
	num += 1

print("")