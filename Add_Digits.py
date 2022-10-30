def add(n):
    c=0
    while n!=0:
        d=n%10
        c+=d
        n=n//10
    return c
m=int(input())
while m>9:
    m=add(m)
print(m)    
        