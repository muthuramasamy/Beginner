# your code goes here
s=input()
l1=[]
l2=[]
for i in range(0,len(s)):
	if i%2==0:
		l1.append(s[i])
	else:
		l2.append(s[i])
a="".join(l1)
b="".join(l2)
print(a,b)
