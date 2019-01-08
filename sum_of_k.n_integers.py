n,k=map(int,input().split(" "))
n1=list(map(int,input().split(" ")))
sum1=0
for k in n1:
	t=n1.pop(0)
	sum1=sum1+t
print(sum1)
