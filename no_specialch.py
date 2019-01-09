n=input()
c=0
for i in n:
	if i.isalnum():
		continue
	else:
		c=c+1
print(c)
