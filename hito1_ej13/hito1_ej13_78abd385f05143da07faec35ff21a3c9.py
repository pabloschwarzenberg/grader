#Factores Primos
 def descomponer_factores_primos(numero):
    factores_primos = []
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return factores_primos

numero = int(input())

factores = descomponer_factores_primos(numero)
for factor in factores:
    print(factor)     