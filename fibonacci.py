n=int(input())
sum1=0
i=0
j=1
print(j,end=" ")
for g in range(n-1):
	sum1=i+j
	i=j
	j=sum1
	if g==n-1:
		print(sum1,end="")
	else:
		print(sum1,end=" ")
