#Factores Primos
n=int(input("ingrese un numero: "))
if n==2:
    print(n)
def descomponer(n):
    primos=[]

    for i in range(2,n):
        while n % i == 0:
            primos.append(i)
            n = n // i
    return primos             
numero=descomponer(n)
for i in range(len(numero)):
    print(numero[i])