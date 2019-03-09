age = input("How old are you?\n\t")

if age:

	age = int(age)

	if(age >= 18 and age < 21):
		print("\nYou  can enter, but you gotta wear a wristband!\n")
	elif (age >= 21):
		print("\nYou're good to go! Go get drunk!\n")
	else:
		print("\nSorry, kid, you can't come in! Go to bed!\n")

else:
	print("\nType in an age, sucker!\n")