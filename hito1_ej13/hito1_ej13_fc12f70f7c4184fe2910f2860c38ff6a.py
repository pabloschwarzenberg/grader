#Factores Primos
n=int(input("ingrese un numero cualquiera: "))
for f in range(2,n+1):
    while n%f==0:
        n=n/f
        print(f)