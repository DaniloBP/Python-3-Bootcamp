
squares = { sqr**2 for sqr in range(10) }
print(squares)

uppers = { char.upper() for char in "hello" }
print(uppers)

strings = "Danilo Pereira"
phrase_vowels = { char for char in strings if char in "aeiou" }
print(phrase_vowels)
print( len(phrase_vowels) )