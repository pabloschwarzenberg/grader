def factorizar_numero(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero /= factor
        else:
            factor += 1

numero = int(input())
factorizar_numero(numero)