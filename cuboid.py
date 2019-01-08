l,b,h=map(int,input().split())
li=[]
sa=(2*l*b)+(2*b*h)+(2*l*h)
vol=l*b*h
li.append(sa)
li.append(vol)
for i in range(0,len(li)):
    print(li[i],end=" ")
    
