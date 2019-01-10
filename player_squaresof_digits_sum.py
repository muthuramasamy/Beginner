n=int(input())
sum1=0
while n>0:
	n1=n%10
	s=n1**2
	sum1=sum1+s
	n=n//10
print(sum1)
