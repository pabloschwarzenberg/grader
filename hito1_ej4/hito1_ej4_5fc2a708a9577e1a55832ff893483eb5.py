n=int(input("Numero: "))
numbs=[]
while True:
    a=n%2
    numbs.append(a)
    n=n//2
    if n==1:
        numbs.append(1)
        numbs.reverse()
        break
print("resultado=",end="")
for i in numbs:
    print(i,end="")