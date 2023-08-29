#Factores Primos
def descomposicion(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor = factor + 1

numero = int(input())

print("Descomposición de factores primos:")
descomposicion(numero)     