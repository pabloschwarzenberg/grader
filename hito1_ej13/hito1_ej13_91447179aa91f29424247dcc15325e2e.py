def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor = factor + 1

# Solicitar al usuario ingresar un número
numero = int(input())

# Imprimir la descomposición de factores primos
descomposicion_factores_primos(numero)
