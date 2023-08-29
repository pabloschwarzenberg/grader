#Factores Primos
def factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            # Si el divisor es un factor primo, lo imprimimos
            print(divisor)
            numero = numero / divisor
        else:
            divisor = divisor + 1

# Solicitamos al usuario que ingrese un número entero
numero = int(input())

# Llamamos a la función para obtener la descomposición en factores primos
factores_primos(numero)
      