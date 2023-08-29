def descomposicion_factores_primos(numero):
    # Lista para almacenar los factores primos
    factores_primos = []

    # Iterar desde 2 hasta la mitad del número
    for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            # Si el número es divisible por 'i', 'i' es un factor primo
            factores_primos.append(i)
            numero = numero // i

    # Si el número que queda después de la división es mayor que 1, también es un factor primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Obtener el número de entrada del usuario
numero = int(input())

# Calcular y imprimir la descomposición de factores primos
descomposicion_factores_primos(numero)