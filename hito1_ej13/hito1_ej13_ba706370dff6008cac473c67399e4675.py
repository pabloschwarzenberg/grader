#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            # Si el divisor es un factor primo, lo imprimimos
            print(divisor)
            numero = numero // divisor
        else:
            # Si no es un factor primo, incrementamos el divisor
            divisor += 1

# Pedimos al usuario que ingrese el número
numero = int(input())

# Realizamos la descomposición de factores primos e imprimimos los resultados
descomposicion_factores_primos(numero)
      