#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor += 1

# Pedir al usuario ingresar un número
numero = int(input())

# Llamar a la función para obtener la descomposición de factores primos
descomposicion_factores_primos(numero)
     