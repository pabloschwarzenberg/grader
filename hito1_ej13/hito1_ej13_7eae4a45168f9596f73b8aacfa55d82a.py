def descomposicion_factores_primos(numero):
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
            numero = numero // divisor
        else:
            divisor += 1

numero = int(input())

descomposicion_factores_primos(numero)