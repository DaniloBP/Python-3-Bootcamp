import random  # use randint(a, b) to generate a random number between a and b

number = None # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = random.randint(1, 10)
    print(f" -----\n {number}\n -----")
    i += 1