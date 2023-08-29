def descomposicion_factores_primos(numero):
    # Inicializar el divisor en 2
    divisor = 2
    
    while divisor <= numero:
        if numero % divisor == 0:
            # El divisor es un factor primo
            print(divisor)
            numero = numero / divisor
        else:
            # Pasar al siguiente posible divisor
            divisor += 1


# Solicitar al usuario un número entero
numero = int(input())

# Realizar la descomposición de factores primos
descomposicion_factores_primos(numero)
