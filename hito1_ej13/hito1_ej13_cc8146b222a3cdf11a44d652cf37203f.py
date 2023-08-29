numero = int(input())

def obtener_factores_primos(n):
    factores = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factores.append(divisor)
            n = n / divisor
        else:
            divisor += 1

    return factores

factores_primos = obtener_factores_primos(numero)

for factor in factores_primos:
    print(factor)
