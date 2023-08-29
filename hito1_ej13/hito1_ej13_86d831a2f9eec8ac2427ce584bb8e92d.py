def factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2
    
    # Mientras el número sea mayor o igual que el divisor
    while numero >= divisor:
        # Si el número es divisible por el divisor
        if numero % divisor == 0:
            # Imprimimos el factor primo
            print(divisor)
            # Dividimos el número por el divisor
            numero = numero / divisor
        else:
            # Avanzamos al siguiente divisor
            divisor += 1

# Pedimos al usuario ingresar un número
numero = int(input())

factores_primos(numero)
