# your code goes here
n=int(input())
sum1=0
while n>0:
	num=n%10
	sum1=sum1+num
	n=n//10
print(sum1)
