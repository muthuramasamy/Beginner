# your code goes here
n=int(input())
c=0
a,b=map(int,input().split())
for i in range(a+1,b):
	if i==n:
		c+=1
		break
if c>0:
	print('yes')
else:
	print('no')
