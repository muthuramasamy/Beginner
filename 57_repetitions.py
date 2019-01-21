# your code goes here
count=0
n,k=map(int,input().split())
p=list(map(int,input().split()))
for i in range(0,len(p)):
	if k==p[i]:
		count=count+1
print(count)
