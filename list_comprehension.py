
# names = ["Mike", "Lucas", "Dustin", "Will", "Eleven", "Max"]
# evens = [2,4,6,8,10,12,14,16,18,20]

# squares = [x*x for x in evens]
# print(squares, end='\n\n')

# uppers = [name.upper() for name in names]
# print(uppers, end='\n\n')

# doubles = [num*2 for num in range(1,6)]
# print(doubles, end='\n\n')

# strings = [str(num) + " times" for num in doubles]
# print(strings, end='\n\n')

# ints = list(range(1,11))

# evens = [num for num in ints if num % 2 == 0]
# print(evens, end='\n\n')

# numbers = [num*num if num % 2 == 0 else num/2 for num in ints]
# print(numbers, end='\n\n')

# with_vowels = "This is awesome!"

# no_vowels = "*".join(char for char in with_vowels if char not in "aeiou")
# print(no_vowels, end='\n\n')

# ---- EXERCISES
answer = [ num for num in [1,2,3,4] if num in [3,4,5,6] ]		# Output --> [3,4]
print(answer)

answer2 = [ name[::-1].lower() for name in ["Elie", "Tim", "Matt"] ]		# Output --> ["eile", "mit", "ttam"]
print(answer2)

answer = [ num for num in range(1,101) if num % 12 == 0 ]		# Output --> [12,24,36,48,...,96]
print(answer)

answer = [char for char in "amazing" if char not in "aeiou"]		# Output --> ['m','z','n','g']
print(answer)