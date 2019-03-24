
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

week = tuple(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

#print(months)
#print(week)

# ACCESSING DATA
print("\nMonths of the year: \n")

for month in months:
	print(f"\t>> {month}")
print()

i = 0
print("\nDays of the week: \n")
while i < len(week):
	print(f"\t>> {week[i]}")
	i += 1
print()

# TUPLES CAN BE USED AS KEYS IN DICTIONARIES!
location = {
	(35.0000, 39.5406) : "Tokyo Office",
	(40.7108, 74.0060) : "San Francisco Office",
	(34.5447, 66.9866) : "Maranguape Office"
}
print(location)

numbers = (1,2,3,4,5,6,3,4,6,6,2)

print(numbers.count(2))
print(numbers.count(6))

print(numbers.index(6))		# Returns the index of the first apperance of the given item in the tuple.

# WE CAN USE  NESTED TUPLES 
# ex_tuple = (1,2,3,(4,5,6,7),8,9,10)

