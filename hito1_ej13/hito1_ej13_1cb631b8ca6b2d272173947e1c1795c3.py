#Factores Primos
def descomponer(a):
    primos=[] 
    for u in range(2, a+1):
        while a%u==0:
            primos.append(u)
            a=a/u
    return primos
a=int(input("ingrese numero:"))
resultado=(descomponer(a))
for item in resultado:
    print(item)