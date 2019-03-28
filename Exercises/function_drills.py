
# EXERCISES ON FUNCTIONS

# A more advanced version of the same function.
def return_day_advanced(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

def return_day(day):
    week = {    1:"Sunday",
                2:"Monday",
                3:"Tuesday",
                4:"Wednesday",
                5:"Thursday",
                6:"Friday",
                7:"Saturday" }
                
    return week.get(day, None)
'''
print(return_day(2))
print(return_day(7))
print(return_day_advanced(-9))
'''

# 2 ----------------------------------

def single_letter_count(word,letter):
    return word.lower().count(letter.lower())

'''
print(single_letter_count("Home", 'o'))
print(single_letter_count("DeeR", 'e'))
print(single_letter_count("DoPE", 'z'))
'''

# 3 -------------------------------------

# flesh out multiple_letter count:
def multiple_letter_count(word):
    return { char : word.count(char) for char in word }

# print(multiple_letter_count("Hello"))

# 4 -----------------------------------

def list_manipulation(a_list, command, location, value=None):
    
    if command == "remove" and location == "end":
        return a_list.pop(-1)
    elif command == "remove" and location == "beginning":
        return a_list.pop(0)
    elif command == "add" and location == "beginning":
        a_list.insert(0,value)
        return a_list
    elif command == "add" and location == "end":
        a_list.append(value)
        return a_list
'''
print( list_manipulation([1,2,3], "remove", "end") )# 3
print( list_manipulation([1,2,3], "remove", "beginning") ) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20) ) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30) ) #  [1,2,3,30]
'''

# 5 -------------------------------------
def is_palindrome(statement):
    statement = statement.replace(" ", "")
    statement = statement.lower()
    
    return statement == statement[::-1]
'''
print( is_palindrome("Hannah") )
print( is_palindrome("a man a plan a canal Panama") )
print( is_palindrome("Hello") )
'''

# 6 -----------------------------------
def frequency(a_list, search_term):
    return a_list.count(search_term)
'''
print( frequency([1,2,3,4,4,4], 4) ) # 3
print( frequency([True, False, True, True], False) ) # 1
print( frequency([True, 'a', 'z', 5, 'a', 7.8], 'a') ) # 2
'''
# 7 -----------------------------------
def capitalize(string):
	first = string[0].upper()
	remaining = string[1::]    
	return (first + remaining)
	# return string[:1].upper() + string[1:]	# Also works

print( capitalize("tim") )# "Tim"
print( capitalize("matt") ) # "Matt")
print( capitalize("a man gotta do what a man gotta do") ) # "Matt")