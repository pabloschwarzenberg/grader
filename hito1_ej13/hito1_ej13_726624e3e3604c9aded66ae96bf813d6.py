#Factores Primos
def factores_primos(numero):
    factores = []

    for i in range(2, int(numero**0.5) + 1):
        while numero % i == 0:
            factores.append(i)
            numero //= i

    if numero > 1:
        factores.append(numero)

    for factor in factores:
        print(factor)

numero = int(input())

factores_primos(numero)