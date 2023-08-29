#Factores Primos
def factorizar_numero(numero):
    # Inicializar el divisor en 2
    divisor = 2
    
    # Mientras el número sea mayor a 1
    while numero > 1:
        # Verificar si el divisor es un factor primo
        if numero % divisor == 0:
            # Imprimir el factor primo
            print(divisor)
            
            # Dividir el número por el factor primo
            numero = numero / divisor
        else:
            # Incrementar el divisor si no es un factor primo
            divisor += 1

# Pedir al usuario que ingrese un número
numero = int(input())

# Realizar la descomposición de factores primos
factorizar_numero(numero)
      