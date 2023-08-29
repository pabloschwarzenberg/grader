def descomposicion_factores_primos(numero):
    factores_primos = []
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    return factores_primos

numero = int(input())

factores_primos = descomposicion_factores_primos(numero)

for factor in factores_primos:
    print(factor)

      