n=int(input())
sum1=0
while n>0:
	a=n%10
	sum1=sum1*10+a
	n=n//10
print(sum1)
