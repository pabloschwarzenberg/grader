def suma_divisores(numero):
    suma = 0
    es_primo = True

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if suma != 1:
        es_primo = False

    return suma, es_primo