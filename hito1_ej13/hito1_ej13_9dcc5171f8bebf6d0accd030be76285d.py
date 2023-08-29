#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            # Si el divisor es un factor primo, lo imprimimos
            print(divisor)
            # Dividimos el número por el divisor para obtener el siguiente número a evaluar
            numero = numero / divisor
        else:
            # Si no es divisible, incrementamos el divisor
            divisor += 1

# Solicitamos el número al usuario
numero = int(input())

# Llamamos a la función para realizar la descomposición en factores primos
descomposicion_factores_primos(numero)
      