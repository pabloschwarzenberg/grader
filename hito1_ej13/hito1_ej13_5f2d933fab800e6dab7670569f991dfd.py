def descomposicion_factores_primos(numero):
    # Inicializar lista para almacenar los factores primos
    factores_primos = []

    # Iterar desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        while numero % i == 0:
            # Agregar el factor primo a la lista
            factores_primos.append(i)
            # Actualizar el número dividiéndolo por el factor primo
            numero //= i

    # Si el número restante después de la descomposición es mayor que 1,
    # significa que es un factor primo en sí mismo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)


# Solicitar al usuario que ingrese un número
numero = int(input())

# Realizar la descomposición de factores primos e imprimir los resultados
descomposicion_factores_primos(numero)
