# your code goes here
n=int(input())
m=0
li=list(map(int,input().split()))
s=li.copy()
li.sort()
t=li.copy()
for i in range(len(li)):
	if s[i]==t[i]:
		m=m+1
	else:
		break
print(m)
