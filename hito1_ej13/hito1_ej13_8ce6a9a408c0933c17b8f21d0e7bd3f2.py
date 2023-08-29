#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2  # Empezamos con el primer número primo
    while factor <= numero:
        if numero % factor == 0:  # Si el número es divisible por el factor
            print(factor)  # Imprimimos el factor primo
            numero = numero // factor  # Actualizamos el número dividiéndolo por el factor
        else:
            factor += 1  # Pasamos al siguiente número primo

# Solicitamos al usuario el número para realizar la descomposición de factores primos
numero = int(input())

# Realizamos la descomposición de factores primos e imprimimos los resultados
descomposicion_factores_primos(numero)      