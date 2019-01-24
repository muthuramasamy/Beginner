s=input()
l1=[]
l2=[]
for i in s:
	if i.isnumeric():
		l1.append(i)
	else:
		l2.append(i)
print("".join(l1))
