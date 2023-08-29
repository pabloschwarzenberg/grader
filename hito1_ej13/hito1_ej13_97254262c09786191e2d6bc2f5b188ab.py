#Factores Primos
def factorizar_numero(numero):
    factor = 2
    while factor * factor <= numero:
        if numero % factor:
            factor += 1
        else:
            numero //= factor
            print(factor)
    if numero > 1:
        print(numero)

numero = int(input())
factorizar_numero(numero)     