k,t=map(int,input().split(" "))
for i in range(k,t):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(j)
  
