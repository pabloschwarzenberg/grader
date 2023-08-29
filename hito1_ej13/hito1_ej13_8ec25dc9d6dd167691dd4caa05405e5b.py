def factorizacion_primos(numero):
    factores_primos = []
    for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            factores_primos.append(i)
            numero = numero // i
    if numero > 1:
        factores_primos.append(numero)
    for factor in factores_primos:
        print(factor)

numero = int(input())
factorizacion_primos(numero)