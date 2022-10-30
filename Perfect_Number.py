def prtsqrt(m):
    n=m
    i=1
    c=0
    while i<n:
        if n%i==0:
            c+=i
        i+=1
    return c
p=int(input()) 
if p==prtsqrt(p):
    print("True")
else:
    print("False")
            
        