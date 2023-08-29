def descomposicion_factores_primos(numero):
    # Inicializar el divisor en 2
    divisor = 2

    # Iterar mientras el número sea mayor a 1
    while numero > 1:
        # Si el número es divisible por el divisor actual
        if numero % divisor == 0:
            # Imprimir el divisor como factor primo
            print(divisor)
            # Dividir el número por el divisor
            numero /= divisor
        else:
            # Incrementar el divisor si no es divisible
            divisor += 1

# Pedir al usuario ingresar un número entero
numero = int(input())

# Llamar a la función de descomposición de factores primos
descomposicion_factores_primos(numero)
