# your code goes here
n=input()
c=0
li=['a','e','i','o','u','A','E','I','O','U']
for i in n:
	for j in li:
		if i==j:
			c+=1
if c>0:
	print('yes')
else:
	print('no')
