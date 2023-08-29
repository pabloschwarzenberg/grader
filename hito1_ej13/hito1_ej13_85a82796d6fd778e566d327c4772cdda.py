#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos la lista de factores primos vacía
    factores_primos = []

    # Iteramos desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        # Verificamos si el número es divisible por i
        while numero % i == 0:
            # Si es divisible, lo agregamos a la lista de factores primos
            factores_primos.append(i)
            # Dividimos el número por i para simplificarlo
            numero //= i

    # Si el número que queda es mayor que 1, también es un factor primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimimos los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Solicitamos al usuario ingresar un número
numero = int(input())

# Llamamos a la función para obtener la descomposición de factores primos
descomposicion_factores_primos(numero)
