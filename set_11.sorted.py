# your code goes here
n=int(input())
m=list(map(int,input().split()))
m.sort()
for i in range(0,len(m)):
	if i==len(m)-1:
		print(m[i],end='')
	else:
		print(m[i],end=' ')
