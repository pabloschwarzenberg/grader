#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        # Verificamos si el divisor es un factor primo
        if numero % divisor == 0:
            # Imprimimos el factor primo
            print(divisor)
            # Dividimos el número por el factor primo
            numero = numero / divisor
        else:
            # Incrementamos el divisor si no es un factor primo
            divisor += 1

# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número entero: "))

# Realizamos la descomposición en factores primos
descomposicion_factores_primos(numero)
      