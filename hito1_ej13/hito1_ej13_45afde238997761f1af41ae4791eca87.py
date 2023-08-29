#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            # Si el número es divisible por el divisor actual, lo imprimimos
            print(divisor)
            # Dividimos el número por el divisor y continuamos el proceso con el cociente
            numero = numero / divisor
        else:
            # Si no es divisible, incrementamos el divisor en 1
            divisor += 1

# Pedimos al usuario que ingrese un número
numero = int(input())

# Imprimimos la descomposición de factores primos del número
descomposicion_factores_primos(numero)
      