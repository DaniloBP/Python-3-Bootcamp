
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

print( is_palindrome("Hannah") )
print( is_palindrome("a man a plan a canal Panama") )
print( is_palindrome("Hello") )