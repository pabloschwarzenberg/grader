def descomposicion_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero /= factor
        else:
            factor += 1

numero = int(input())
descomposicion_primos(numero)
