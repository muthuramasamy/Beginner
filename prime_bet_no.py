k,t=map(int,input().split(" "))
li=[]
for i in range(k+1,t):
	if i>1:
		for j in range(2,i):
			if i%j ==0:
				break
		else:
			li.append(i)
for i in range (0,len(li)):
	if (li[i]==i):
		print(li[i],end="")
	else:
		print(li[i],end=" ")
  
