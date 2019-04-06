nums = [2,4,6,8,10]
nums.reverse()	# .reverse() it's a list method and reverse the list in place.
print(nums)

nums_revsrd = list( reversed(nums) )	# reversed() returns a reverseiterable object. It'll reverse any iterable object. 
# In fact it doesn't make sense to convert it to a list, but it's just for ilustration.
print(nums_revsrd)

person = "Python is cool"
for char in reversed(person):
	print(char)

print()

for num in reversed( range(0,10) ):
	print(num)