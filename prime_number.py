a=int(input())
ram=0
for i in range(2,a+1):
    if a%i==0:
        ram+=1
if ram<=2:
    print("prime")
else:
    print("not a prime")