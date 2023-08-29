#Factores Primos
x = int(input("introduzca un numero: "))


def descomponer(n):
    primos = []

    for j in range(2, n + 1):
        while n % j == 0:
            primos.append(j)
            n = n / j

    for j in range(len(primos)):
        print(primos[j])

descomponer(x)