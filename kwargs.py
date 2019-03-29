# kwargs stands for 'keyword args'

def numbers(**kwargs):
	for key, value in kwargs.items():
		print(f"{key} --> {value}")

# numbers(one=1, two=2, three=3, four=4, five=5)

# EXERCISE -------------
# Define combine_words below:
def combine_words(word, **kwargs):
    for key, value in kwargs.items():
        if "prefix" in key:
            return (value + word)
        elif "suffix" in key:
            return (word + value)
    return word

'''
def combine_words(word, **kwargs):		# Also works
    if "prefix" in kwargs:
        return (kwargs["prefix"] + word)
    elif "suffix" in kwargs:
        return (word + kwargs["suffix"])
    return word
'''

print( combine_words("home"))	# home
print( combine_words("home", suffix="less"))	# homeless
print( combine_words("child", prefix="man")	# manchild
print( combine_words("work", prefix="home"))	# homework

