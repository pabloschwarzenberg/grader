#Factores Primosdef descomposicion_factores_primos(numero):
def descomposicion_factores_primos(numero):
    # Inicializar el divisor con el valor más pequeño
    divisor = 2

    while numero > 1:
        # Verificar si el divisor actual es un factor primo
        while numero % divisor == 0:
            # Imprimir el factor primo encontrado
            print(divisor)
            numero //= divisor

        # Incrementar el divisor para buscar el siguiente factor primo
        divisor += 1

# Solicitar al usuario ingresar un número
numero = int(input())

# Realizar la descomposición de factores primos
descomposicion_factores_primos(numero)
    