n=int(input())
li=list(map(int,input().split(" ")))
li.sort()
for i in range(0,len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
	
