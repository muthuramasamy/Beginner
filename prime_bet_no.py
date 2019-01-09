li=[]
def ch(b):
	a1=str(b)
	tlen=len(a1)
	amst=0
	b1=b
	while(b>0):
		t=b%10
		t1=(t**tlen)
		amst=amst+t1
		b=b//10
	if(b1==amst):
		li.append(amst)
l,k=map(int,input().split(" "))
for i in range(l+1,k):
	ch(i)
for i in range(len(li)):
	if(i==len(li)-1):
		print(li[i],end="")
	else:
		print(li[i],end=" ")
