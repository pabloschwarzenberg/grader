# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo
