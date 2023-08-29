#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializar el divisor en 2
    divisor = 2

    # Ciclo para encontrar los factores primos
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

# Solicitar al usuario que ingrese un número
numero = int(input())

# Descomponer los factores primos del número ingresado
descomposicion_factores_primos(numero)

      