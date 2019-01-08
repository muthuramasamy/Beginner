n=int(input())
sum1=1
while n > 0:
    b=n%10
    sum1=sum1*b
    n=n//10
print(sum1)
