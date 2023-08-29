def suma_divisores(numero):
    suma = 0
    divisor = 1
    while divisor * divisor <= numero:
        if numero - (numero // divisor) * divisor == 0:
            suma += divisor
            if divisor != numero // divisor:
                suma += numero // divisor
        divisor += 1

    es_primo = suma == numero + 1

    return suma, es_primo