
l1 = [1,2,3,4]
l2 = [5,6,7,8]

z = zip(l1, l2)
# print(z)

zip_list = list(z)
# print(zip_list)

l3 = [10,11,12,13,14,15,16]

z = zip(l3,l1)
zip_list = list(z)
# print(zip_list)

words = ["library", "bus station", "mall", "hostel"]

z = zip(words, l1, l3)
zip_list = list(z)
# print(zip_list)

z = zip(l1,l2)
zip_list = list(z)	# [(1,5), (2,6), (3,7), (4,8)]
unziped = list(zip(*zip_list))
print(unziped)	# [(1,2,3,4), (5,6,7,8)]

