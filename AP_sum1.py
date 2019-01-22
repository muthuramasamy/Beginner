n,a,d=map(int,input().split())
li=[]
if d!=0:
	for i in range(a,n+1,d):
		li.append(i)
print(sum(li))
