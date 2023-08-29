#Factores Primos
def descomponer(n):
    primos = []
    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    for i in primos:
        print(i)
n = int(input('Ingresa un numero:'))
descomponer(n)      