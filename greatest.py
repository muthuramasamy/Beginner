n,o,p=map(int,input().split(" "))
f=0
if n>=p and n>=o:
	print(n)
	f=1
elif o>=p and o>=n and f==0:
	print(o)
	f=1
elif p>=n and p>=o and f==0:
	print(p)
