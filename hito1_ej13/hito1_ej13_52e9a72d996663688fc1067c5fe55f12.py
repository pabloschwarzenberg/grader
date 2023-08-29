#Factores Primos
def factorizar(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        # Si el número es divisible por el divisor actual, lo imprimimos y lo dividimos
        if numero % divisor == 0:
            print(divisor)
            numero = numero / divisor
        else:
            # Si no es divisible, incrementamos el divisor
            divisor += 1

# Solicitamos al usuario que ingrese un número entero
numero = int(input())

# Llamamos a la función para factorizar el número
factorizar(numero)
      