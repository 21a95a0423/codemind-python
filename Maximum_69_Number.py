n=int(input())
a=str(n)
b=1
for i in a:
    if int(i)==6 and b==1:
        i=9
        b=0
    print(i,end="")    