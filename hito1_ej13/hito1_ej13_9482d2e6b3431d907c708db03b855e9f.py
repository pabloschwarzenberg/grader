#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos una lista vacía para almacenar los factores primos
    factores_primos = []

    # Iteramos desde 2 hasta la mitad del número, buscando los factores primos
    for i in range(2, int(numero/2) + 1):
        # Verificamos si el número es divisible por i
        while numero % i == 0:
            # Si es divisible, añadimos i a la lista de factores primos
            factores_primos.append(i)
            # Dividimos el número entre i
            numero = numero / i

    # Si el número restante después de la factorización es mayor a 1, entonces es primo
    if numero > 1:
        factores_primos.append(int(numero))

    # Imprimimos los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Pedimos al usuario que ingrese un número
numero = int(input())

# Llamamos a la función para realizar la descomposición de factores primos
descomposicion_factores_primos(numero)
      