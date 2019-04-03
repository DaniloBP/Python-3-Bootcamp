
nums = range(0,21)

odds = filter( lambda num : num % 2 != 0, nums)
print(odds)

print(list(odds))