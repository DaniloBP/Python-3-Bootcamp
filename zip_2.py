midterms = [80,88,79]
finals = [96,77,81]
students = ["Ruben", "Monse", "Jamal"]

final_grades_list = [ elem for elem in zip(students, midterms, finals) ]
# print(final_grades_list)

# final_grades_dict = { elem[0]: max(elem[1], elem[2]) for elem in zip(students, midterms, finals) }
final_grades_dict = { elem[0]: (elem[1], elem[2]) for elem in zip(students, midterms, finals) }
# print(final_grades_dict)

# grades = map( lambda elem: max(elem), zip(midterms, finals) )
# grades = map( lambda elem: (elem[0], elem[1], elem[2]), zip(students, midterms, finals) )
# grades = map( lambda elem: (elem[0], max(elem[1], elem[2])), zip(students, midterms, finals) )

grades = zip(
			students,
			map( lambda elem: max(elem), zip(midterms, finals) )
		)
# print(list(grades))
# print(dict(grades))

# -------------- EXERCISE -------------------
# 1)
def interleave(string1, string2):
    return "".join([ "".join(tup) for tup in zip(string1, string2) ])

# print( interleave("hi", "ha"))		# "hhia"
# print( interleave("aaa", "zzz"))	# "azazaz"
# print( interleave("lzr", "iad"))	# "lizard"

# 2)
def triple_and_filter(nums):
    return [ 3*num for num in filter( lambda num : num % 4 == 0, nums) ]

# print(triple_and_filter([1,2,3,4])) # [12]
# print(triple_and_filter([6,8,10,12])) # [24,36]

# 3)
def extract_full_name(names):
    return [ name for name in map( lambda elem: elem["first"] + " " + elem["last"], names) ]

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) 	# ['Elie Schoppik', 'Colt Steele']
names = [{'first': 'Dan', 'last': 'Smith'}, {'first': 'Cathy', 'last': 'Johnson'}]
print(extract_full_name(names)) 	# ['Dan Smith', 'Cathy Johnson']