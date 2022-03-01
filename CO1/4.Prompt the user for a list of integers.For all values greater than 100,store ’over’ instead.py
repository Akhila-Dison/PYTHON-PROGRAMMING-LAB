integers=int(input("Enter the limit:"))
temp=[]
over=0
for i in range(0,integers):
	user=int(input("Enter a number:"))
	if(user>=100):
		temp.append(user)
	else:
		temp.append(over)
print("List elements are",temp)
