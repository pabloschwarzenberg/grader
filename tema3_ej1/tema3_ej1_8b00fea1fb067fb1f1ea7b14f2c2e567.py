def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        es_primo = True
    else:
        es_primo = False

    return suma, es_primo
