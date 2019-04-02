
def sumAll(*args):		# args its a tuple
	print(args)
	total = 0
	for num in args:
		total += num
	print(total) 

# sumAll(4,5,6,7,8,9)	# 39

nums1 = [4,5,6,7,8,9]
# sumAll(nums1)		# It'll throw an ERROR.
 
nums2 = (1,2,3,4,5,6)
# sumAll(nums1)		# It'll throw the same ERROR.

# sumAll(*nums1)		# It'll work now. '*' unpacks all values in nums and  pass them individually.
# sumAll(*nums2)		# It'll work now.

def display_name(first, last):
	print(f"Hello, {first} {last}")

names = {"first" : "Black", "last" : "Panther"}
# display_name(names)		# Nope...
# display_name(**names)		# '**' unpacks dict each keyword argument.

def multiply_and_add(a, b, c):
	print(a + b * c)

data = {'a' : 5, 'b' : 10, 'c' : 20}

# multiply_and_add(**data)	# '**' UNPACKS DICTIONARY CONTENT.

def show_data(**kwargs):		# In the declaration of the function it will get the data and pack it into a dictionary.
	print(kwargs)

# show_data(name="Thales", age=34, country="Canada")

# ------------ EXERCISES ----------------
def calculate(**kwargs):
    result = None
    message = None

    if kwargs["operation"]=="add":
        result = kwargs["first"] + kwargs["second"]
    elif kwargs["operation"]=="subtract":
        result = kwargs["first"] - kwargs["second"]
    elif kwargs["operation"]=="multiply":
        result = kwargs["first"] * kwargs["second"]
    else:
        result = kwargs["first"] / kwargs["second"]

    if kwargs["make_float"] == True:
    	result = float(result)
    else:
    	result = int(result)

    if kwargs.get("message"):
    	message = kwargs["message"]
    else:
    	message = "The result is"

    return message + " " + str(result)

print( calculate(make_float=False, operation='add', message='You just added', first=2, second=4) )	# "You just added 6"
print( calculate(make_float=True, operation='divide', first=3.5, second=5) )	 # "The result is 0.7"