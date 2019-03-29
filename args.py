
def sum(*args):		# args is a Tuple
	total = 0
	for num in args:
		total += num
	return total

print( sum(2,4,5,8) ) # 19
print( sum(10,-8) )	# 2
print( sum(10,9,8,7,6,5,4,3,2,1) )	# 55
# -------------------------------------------------------------
def check_user(*data):
	if "Danilo" in data and "Batista" in data:
		return "Welcolme back, master."
	return "Get the f.. outta here, intruder!!".upper()

print( check_user("Danilo", 54, True, "great", None, []))
print( check_user("Danilo", True, "grrrrrrr", {}, "Batista"))