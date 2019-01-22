#hey guvi
a,d,n=map(int,input().split())
k=[]
if d!=0:
	for i in range(a,n+1,d):
		k.append(i)
	print(sum(k))
