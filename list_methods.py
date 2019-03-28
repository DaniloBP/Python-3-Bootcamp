numbers = [1, 2, 3, 4]
numbers.append(5)
print(f"\nList after append: {numbers}\n")

# numbers.append(5, 6, 7)   Won't work.
# 
# It will treat this list as a single element of type "List"
numbers.append([6, 7, 8])  
print(f"\nList after append a list: {numbers}\n")

# This will work just fine
numbers.extend([9,10,11,12])
print(f"\nList after .extend() a list: {numbers}\n")

numbers.insert(-1, "the end")
print(f"\nList after the first .insert() a list: {numbers}\n")

numbers.insert(5, "Third item")
#print(f"\nList after the second .insert() a list: {numbers}\n")

# colors = ['blue', 'red', 'yellow', 'green']
# print(colors)

# colors.clear()   # Deletes all items in a list
# print(colors)

# colors = ['blue', 'red', 'yellow', 'green']

# last_item = colors.pop()		# If no parameter is passed, removes and returns the last item in the list.

# print(f'\nThe removed item was -->  {last_item}\n')

# colors.pop(0)		# Removes the item at the given index.

# print(f'\n{colors}\n')

# colors.remove('red')		# Removes the first occurrence of the passed element from the list.

# print(f'\n{colors}\n')

index = numbers.index(4)		# Returns the index of the first occurrence of '4'
print(f"\nFirst occurrence of '4' in the list: {index}\n")

numbers.extend([4,4,5,6])
print(f"\n{numbers}\n")

# The second parameter says in which index search of the given item must be started. 
index = numbers.index(4, 4)		# Returns the index of the first occurrence of '4' starting at index [4]
print(f"\nSecond occurrence of '4' in the list: {index}\n")

index = numbers.index(5, 10, 15)		# Returns the index of the first occurrence of '5' between indexes [10] to [15]
print(f"\nFirst occurrence of '5' between indexes [10] to [15]: {index}\n")

print(f"List size: {len(numbers)}\n")

count = numbers.count(20)	# Returns how many times the element passed occurs in the list.
print(f"Count: {count}\n")

second = [1,2,3,4,5]
print(f'\nRegular order: {second}\n')

second.reverse()
print(f'\nReversed order: {second}\n')

second = [6,9,5,3,7,1,4,2]
print(f'\nUnordered list: {second}\n')

second.sort()
print(f'\nSorted list: {second}\n')   

words = ['Lebron', '\"The Chosen One\"', 'James']
space = " "
new_name = space.join(words)		# It puts the list 'words' together and add a white space between the elements. Returns a new string.

print("\n"+ new_name + "\n")