k=int(input())
m=0
n=1
t=0
while m<k:
    t=m
    m=n
    n=t+m
    if n>k:
        break
    
a=abs(m-k)
b=abs(n-k)
if a==b:
    print(m,n)
elif a<b:
    print(m)
else:
    print(n)
       