# completa el código de la función
def suma_divisores(a):
    primo = False
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i

    if suma == 1:
        primo = True

    return suma, primo