def descomposicion_factores_primos(numero):
    # Inicializar el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            # Si el divisor es un factor primo, imprimirlo
            print(divisor)
            # Dividir el número por el divisor y actualizar su valor
            numero = numero / divisor
        else:
            # Si no es divisible, incrementar el divisor
            divisor = divisor + 1

# Pedir al usuario ingresar un número
numero = int(input())

# Calcular la descomposición en factores primos del número
descomposicion_factores_primos(numero)
