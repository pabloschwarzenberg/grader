# completa el código de la función
def suma_divisores(a):  # No se debe incluir al mismo número
    suma = 0
    for i in range(1, a):
        if a % i == 0:
           suma += i
    if suma == 1:
        return suma, True
    return suma, False