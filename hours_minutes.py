# your code goes here
n=int(input())
if n<60:
	t=n%60
	print('0',t)
else:
	p=n//60
	q=n%60
	print(p,q)
