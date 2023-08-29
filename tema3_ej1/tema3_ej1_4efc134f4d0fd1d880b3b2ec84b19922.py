# completa el código de la función
def suma_divisores(a):
    suma = 0

    for divisor in range(1, a):
        if a % divisor == 0:
            suma += divisor

    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo
           