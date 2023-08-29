#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor += 1

# Solicitar al usuario ingresar el número entero
numero = int(input())

# Realizar la descomposición en factores primos e imprimir los resultados
descomposicion_factores_primos(numero)
