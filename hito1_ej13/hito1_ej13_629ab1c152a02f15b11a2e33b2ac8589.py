#Factores Primos
numero = int(input("Ingrese numero: "))


def descomponer(p):
    primos = []

    for i in range(2, p + 1):
        while p % i == 0:
            primos.append(i)
            p = p / i
            
    for i in range(len(primos)):
        print(primos[i])

descomponer(numero)     