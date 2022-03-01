cyear=int(input("The current year:"))
fyear=int(input("The final year:"))
print("Leap year between",cyear,"and",fyear)
for i in range (cyear,fyear):
	if i%4==0:
		print(i)
