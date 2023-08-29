#Factores Primos
n=int(input("Ingrese un número:"))
a=2
while n!=1:
    if n%a==0:
        print(a)
        n=n/a
    else:
        a=a+1
