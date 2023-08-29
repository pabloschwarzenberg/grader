#Factores primos
def descomposicion_factores_primos(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor += 1

# Pedir al usuario que ingrese un número
numero = int(input())

# Calcular y mostrar la descomposición en factores primos
descomposicion_factores_primos(numero)