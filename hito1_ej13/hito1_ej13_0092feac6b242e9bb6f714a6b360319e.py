#Factores Primos
def descomponer_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1

# Solicitar al usuario ingresar un número
numero = int(input())

# Descomponer el número en factores primos e imprimirlos
descomponer_factores_primos(numero)
     