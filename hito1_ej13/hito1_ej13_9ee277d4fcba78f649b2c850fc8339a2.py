def descomposicion_factores_primos(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1

# Obtener el número del usuario
numero = int(input())

# Calcular y mostrar la descomposición de factores primos
descomposicion_factores_primos(numero)

      