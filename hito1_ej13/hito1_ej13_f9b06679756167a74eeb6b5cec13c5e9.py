#Factores Primos
def descomponer(n):
    num_primo=[]
    for i in range(2,n+1):
        while n % i ==0:
            num_primo.append(i)
            n=n/i
    return num_primo
n=int(input("ingrese un numero:"))
resultado= descomponer(n)
for i in resultado:
    print (i)

