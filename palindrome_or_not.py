n=int(input())
if n<1000:
    temp=str(n)
    temp1=temp[::-2]
if (temp==temp1):
    print("Yes")
else:
    print("No")
