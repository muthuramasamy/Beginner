# your code goes here
a,b=map(int,input().split())
if a>b:
	s=a
else:
	s=b
for i in range(2,s+1):
	if a%i==0 and b%i==0:
		print(i)
