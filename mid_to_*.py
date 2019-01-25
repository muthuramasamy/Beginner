# your code goes here
s=input()
p=len(s)
mid=0
mid1=0
l1=[]
for i in s:
	l1.append(i)
if p%2!=0:
	mid=p//2
	l1[mid]="*"
	print("".join(l1))
else:
	mid=p//2
	mid1=mid-1
	l1[mid]="*"
	l1[mid1]="*"
	print("".join(l1))
