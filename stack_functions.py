n=[]
m=int(input())
k=int(input())
l=int(input())
def empty():
    if (len(n)==0):
        print("The Stack is Empty")
def push():
    if (len(n)< m):
        for i in range  (0,k):
            n.append(i)
    print(n)
def pop():
    if(len(n)>= m):
        for j in range(0,l):
            n.remove(n[j])
    print(n)
empty()
push()
pop()

