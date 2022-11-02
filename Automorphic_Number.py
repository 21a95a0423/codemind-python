n=int(input())
k=n**2
a=str(n)
b=str(k)
c=len(a)
if a==b[-c:]:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")