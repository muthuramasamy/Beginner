# your code goes here
a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
	if i%2!=0:
		c=c+1
		if c==b:
			break
	else:
		continue
print(l[c])
