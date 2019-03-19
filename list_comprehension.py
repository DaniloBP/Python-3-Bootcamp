
names = ["Mike", "Lucas", "Dustin", "Will", "Eleven", "Max"]
evens = [2,4,6,8,10,12,14,16,18,20]

squares = [x*x for x in evens]
print(squares, end='\n\n')

uppers = [name.upper() for name in names]
print(uppers, end='\n\n')

doubles = [num*2 for num in range(1,6)]
print(doubles, end='\n\n')

strings = [str(num) + " times" for num in doubles]
print(strings)