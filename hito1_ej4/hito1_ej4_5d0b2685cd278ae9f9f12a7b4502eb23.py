n=int(input("Ingrese un número entero en sistema decimal:"))
b=int(0)
l=int(0)
while n>1:
    a=int(n%2)
    n=int(n//2)
    b=(b)+((10**l)*a)
    l+=1
if n==1:
    print("resultado=",int(10**l)+b)
if n==0:
    print("resultado=",0)
