
# numbers = dict( first = 1, second = 2, third = 3, fourth = 4, fifth = 5)

# squares = { key : value ** 2 for key, value in numbers.items() }
# print(squares)

# new_dict = { num : num ** 2 for num in [6,7,8,9,10] }
# print(new_dict)

# str1 = "ABC"
# str2 = "123"
# new_dict = { str1[i] : str2[i] for i in range(0, len(str1)) }
# print(new_dict)

# list1 = ['a', 'b', 'c', 'd', 'e']
# list2 = [1,2,3,4,5]
# new_dict = { list1[i] : list2[i] / 2 for i in range(0, len(list2)) }
# print(new_dict)

# new_dict = { num : ("even" if num % 2 == 0 else "odd") for num in range(1,11) }		# Conditional logic in dictionary comprehension can be applied to keys and values.
# print(new_dict)

# EXERCISE 1

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = { person[i][0] : person[i][1] for i in range(0, len(person)) }		# My solution

# answer = {thing[0]: thing[1] for thing in person}		# Solution #2

# answer = {k:v for k,v in person}						# Solution #3

# If you have a list of pairs, you can very easily turn it into a dictionary using dict()
# answer = dict(person)									# Solution #4

print(answer)

# EXERCISE 2

answer = { vow : 0 for vow in ['a', 'e', 'i', 'o', 'u'] }
print(answer)

# EXERCISE 3

answer = { ascii : chr(ascii) for ascii in range(65, 91) }
print(answer)