a,b=map(int,input().split())
if a>b:
    l=a
else:
    l=b
v=l
while l!=0:
    if l%a==0 and l%b==0:
        print(l)
        break
    else:
        l=l+v
    