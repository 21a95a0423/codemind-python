def rev(n):
    c=0
    while n:
        d=n%10
        c=c*10+d
        n=n//10
    return c
#square
def squ(n):
    return n*n
n=int(input())
a=squ(n)
b=squ(rev(n))
if a==rev(b):
    print("True")
else:
    print("False")