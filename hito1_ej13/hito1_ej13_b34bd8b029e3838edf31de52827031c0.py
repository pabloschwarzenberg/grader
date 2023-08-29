#Factores Primos
def factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor = factor + 1

numero = int(input())
factores_primos(numero)
     