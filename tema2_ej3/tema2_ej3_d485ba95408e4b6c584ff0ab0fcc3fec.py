def es_numero_perfecto(numero):
    import random
    numero = random.randint (0,1000)
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero