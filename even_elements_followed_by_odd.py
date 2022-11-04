n=int(input())
s=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(s)):
    if s[i]%2==0:
        a.append(s[i])
    else:
        b.append(s[i])
for k in range(len(b)):
    a.append(b[k])
for j in range(len(a)):
    print(a[j],end=" ")