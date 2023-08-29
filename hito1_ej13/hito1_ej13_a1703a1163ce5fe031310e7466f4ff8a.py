def dfp(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor = factor + 1


numero = int(input())

print('Descomposición en factores primos: ')
dfp(numero)
