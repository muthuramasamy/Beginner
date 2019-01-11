n=int(input())
m=list(map(int,input().split()))
m.sort()
#print(m)
li=m[::-1]
for i in range(len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end="")
