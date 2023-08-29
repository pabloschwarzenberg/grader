def descomposicion_factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
            numero = numero / divisor
        else:
            divisor += 1

# Pedimos al usuario que ingrese un número
numero = int(input())

# Llamamos a la función para imprimir la descomposición de factores primos
descomposicion_factores_primos(numero)

      