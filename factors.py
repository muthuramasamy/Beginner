# your code goes here
n=int(input())
li=[]
for i in range(1,n+1):
	if n%i==0:
		li.append(i)
	else:
		continue
for i in range(0,len(li)):
	if i==len(li)-1:
		print(li[i],end='')
	else:
		print(li[i],end=' ')
