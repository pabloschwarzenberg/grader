#Descomponer un número
def descomponer (n):
    primos=[]
    for i in range (2,n+1):
        while n%i == 0:
            primos.append(i)
            n=n/i
    return primos
        
num=int(input("Ingrsea un Numero para descomponer :"))
print(descomponer(num))