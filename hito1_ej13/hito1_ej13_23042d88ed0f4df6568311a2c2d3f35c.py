def descomposicion_factores_primos(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1

# Pedir al usuario ingresar el número
numero = int(input())

# Imprimir la descomposición en factores primos
descomposicion_factores_primos(numero)
