#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos una lista vacía para almacenar los factores primos
    factores_primos = []

    # Comenzamos a buscar factores primos desde el número 2
    divisor = 2
    while divisor <= numero:
        # Si el número es divisible por el divisor actual, es un factor primo
        if numero % divisor == 0:
            # Agregamos el factor primo a la lista
            factores_primos.append(divisor)
            # Dividimos el número por el factor primo encontrado
            numero = numero // divisor
        else:
            # Si no es divisible, incrementamos el divisor en 1
            divisor += 1

    # Imprimimos los factores primos
    for factor in factores_primos:
        print(factor)

# Pedimos al usuario que ingrese un número entero
numero = int(input())

# Llamamos a la función para realizar la descomposición en factores primos
descomposicion_factores_primos(numero)      