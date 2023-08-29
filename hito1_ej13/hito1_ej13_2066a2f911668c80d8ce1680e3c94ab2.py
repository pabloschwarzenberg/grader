#Factores Primos
n = int(input("Ingrese numero: "))

def descomponer(n):
    primos = []
    
    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n // i
    return primos

numeros_primos = descomponer(n)

for factores in numeros_primos:
    print(factores)
      