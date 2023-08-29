def descomposicion_factores_primos(numero):
    # Inicializar lista para almacenar los factores primos
    factores_primos = []

    # Comenzar desde el factor primo más pequeño, que es 2
    factor = 2

    # Iterar mientras el número sea mayor que 1
    while numero > 1:
        # Verificar si el factor es divisor del número
        if numero % factor == 0:
            # Agregar el factor a la lista
            factores_primos.append(factor)
            
            # Dividir el número por el factor
            numero = numero // factor
        else:
            # Incrementar el factor si no es divisor del número
            factor += 1

    # Imprimir los factores primos en líneas separadas
    for factor_primo in factores_primos:
        print(factor_primo)

# Pedir al usuario que ingrese un número
numero = int(input())

# Llamar a la función para obtener la descomposición de factores primos
descomposicion_factores_primos(numero)