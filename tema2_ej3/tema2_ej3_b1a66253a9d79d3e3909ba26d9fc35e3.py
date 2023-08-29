def numero_perfecto(numero):
    suma = sum([i for i in range(1, numero) if numero % i == 0])

    return suma == numero
