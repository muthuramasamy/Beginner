# your code goes here
st=input()
a=0
b=0
for i in st:
	if i.isalpha():
		a=a+1
	elif i.isnumeric():
		b=b+1
	else:
		continue
if a>0 and b>0:
	print('Yes')
else:
	print('No')
