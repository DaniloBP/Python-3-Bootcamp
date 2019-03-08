print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)

#print(f"OK, you ran {miles} miles" .format(miles))
print(f"OK, {kms} kilometers is equal to {miles} miles" )