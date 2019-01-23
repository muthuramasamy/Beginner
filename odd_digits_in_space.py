#heyguvi
n=int(input())
li=[]
while n>0:
	t=n%10
	if t%2!=0:
		li.append(t)
	n=n//10
li.sort()
for i in range(len(li)):
	if i==len(li)-1:
		print(li[i],end='')
	else:
		print(li[i],end=' ')
