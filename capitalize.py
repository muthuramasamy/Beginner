# your code goes here
n=list(map(str,input().split()))
li=[]
for i in range(len(n)):
	k=n[i].capitalize()
	li.append(k)
for i in range(0,len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
	
