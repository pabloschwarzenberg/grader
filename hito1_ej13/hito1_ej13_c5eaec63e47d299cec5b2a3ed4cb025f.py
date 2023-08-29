#Factores Primos
def factorizar(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    # Mientras el número sea mayor a 1
    while numero > 1:
        # Si el número es divisible por el divisor actual
        if numero % divisor == 0:
            # Imprimimos el divisor
            print(divisor)
            # Dividimos el número por el divisor
            numero = numero / divisor
        else:
            # Si no es divisible, incrementamos el divisor
            divisor += 1

# Solicitamos al usuario el número a factorizar
numero = int(input())

# Llamamos a la función para factorizar el número
factorizar(numero)
      