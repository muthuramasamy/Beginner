a=int(input())
t=str(a)
p=len(t)
c=0
a1=a
while a>0:
	y=a%10
	b=y**p
	c=c+b
	a=a//10
print(c)
if a1==c:
	print("yes")
else:
	print("no")
