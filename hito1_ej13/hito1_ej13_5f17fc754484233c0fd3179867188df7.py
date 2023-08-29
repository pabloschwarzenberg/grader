def factores_primos(numero):
    # Inicializar el divisor en 2
    divisor = 2
    
    # Ciclo para encontrar los factores primos
    while divisor <= numero:
        # Verificar si el divisor es un factor primo
        if numero % divisor == 0:
            # Imprimir el factor primo
            print(divisor)
            
            # Actualizar el número dividiéndolo por el factor primo
            numero //= divisor
        else:
            # Incrementar el divisor si no es un factor primo
            divisor += 1

# Pedir al usuario que ingrese un número
numero = int(input())

# Calcular y mostrar la descomposición en factores primos
factores_primos(numero)
      