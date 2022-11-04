n=int(input())
s=list(map(int,input().split()))
a=[]
b=[]
for i in s:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
for j in a:
    b.append(j)
for k in b:
    print(k,end=" ")