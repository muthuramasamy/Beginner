# your code goes here
s=input()
s1=s.lower()
l1=[]
c=0
for i in s1:
	if i.isalpha():
		if i in l1:
			c=c+1
		l1.append(i)
if c>1:
	print('No')
else:
	print('Yes')
