def descomposicion_factores_primos(numero):
    # Inicializar lista para almacenar los factores primos
    factores_primos = []

    # Comenzar con el factor primo más pequeño, que es 2
    factor = 2

    # Realizar la descomposición de factores primos
    while factor <= numero:
        if numero % factor == 0:
            factores_primos.append(factor)
            numero = numero / factor
        else:
            factor += 1

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Solicitar al usuario ingresar un número entero
numero = int(input())

# Llamar a la función para obtener la descomposición de factores primos
descomposicion_factores_primos(numero)