# completa el código de la función
def suma_divisores(a):
    suma = 0
    primo = True
    for divisor in range(1, a):
        if a % divisor == 0:
            suma += divisor
    if suma != 1:
        primo = False
    return suma, primo    