#Factores Primos
def factorizar(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor += 1

numero = int(input('Ingrese un numero entero: '))
factorizar(numero)
