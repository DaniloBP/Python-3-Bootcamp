numbers = [1, 2, 3, 4]
numbers.append(5)
print(f"\nList after append: {numbers}\n")

# numbers.append(5, 6, 7)   Won't work.
# 
# We'll treat this list as a single element of type "List"
numbers.append([6, 7, 8])  
print(f"\nList after append a list: {numbers}\n")

# This will work just fine
numbers.extend([9,10,11,12])
print(f"\nList after .extend() a list: {numbers}\n")

print(f"List size: {len(numbers)}\n")

numbers.insert(-1, "the end")
print(f"\nList after the first .insert() a list: {numbers}\n")

numbers.insert(3, "Third item")
print(f"\nList after the firsecond .insert() a list: {numbers}\n")

colors = ['blue', 'red', 'yellow', 'green']
print(colors)

colors.clear()   # Deletes all items in a list
print(colors)

colors = ['blue', 'red', 'yellow', 'green']

last_item = colors.pop()		# If no parameter is passed, removes and returns the last item in the list.

print(f'\nThe removed item was -->  {last_item}\n')

colors.pop(0)		# Removes the item at the given index.

print(f'\n{colors}\n')

colors.remove('red')		# Removes the first ocurrence of the passed element from the list.

print(f'\n{colors}\n')

index = numbers.index(4)

print(f'\n{index}\n')


