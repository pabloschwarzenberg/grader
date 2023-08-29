# completa el código de la función
def suma_divisores(a):
    suma = 0

    for divisor in range(1, a):
        if a % divisor == 0:
            suma += divisor

    es_primo = suma == 1

    return suma, es_primo
