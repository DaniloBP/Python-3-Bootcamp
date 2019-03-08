print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)

#print("OK, you ran {miles} miles" .format(miles))
if miles <= 10.0:
	print(f"\nOK, good run.\t({kms} kilometers is equal to {miles} miles)\n" )
elif miles <= 15.0:
	print(f"\nOK, I see you! Great run, my brother\\sister.\t({kms} kilometers is equal to {miles} miles)\n" )
else:
	print(f"\nDamn, son!!! You went full Kenian mode today, my man.\t({kms} kilometers is equal to {miles} miles)\n" )
