
def sumAll(*args):		# args its a tuple
	print(args)
	total = 0
	for num in args:
		total += num
	print(total) 

sumAll(4,5,6,7,8,9)	# 39

nums1 = [4,5,6,7,8,9]
# sumAll(nums1)		# It'll throw an ERROR.
 
nums2 = (1,2,3,4,5,6)
# sumAll(nums1)		# It'll throw the same ERROR.

sumAll(*nums1)		# It'll work now. '*' unpacks all values in nums and  pass them individually.

sumAll(*nums2)		# It'll work now.