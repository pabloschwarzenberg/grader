def descomposicion_factores_primos(numero):
    # Función para encontrar los factores primos de un número
    factores_primos = []
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero = numero / divisor
        else:
            divisor = divisor + 1

    return factores_primos


# Solicitar al usuario ingresar un número
numero = int(input())

# Obtener los factores primos del número
factores_primos = descomposicion_factores_primos(numero)

# Imprimir los factores primos en líneas separadas
for factor in factores_primos:
    print(factor)
    