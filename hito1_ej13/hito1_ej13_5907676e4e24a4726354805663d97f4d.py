#Factores Primos
def descomponer(n):
    primos = []
    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    for valor in primos:
        print(valor)
    return primos
a = int(input())
(descomponer(a))