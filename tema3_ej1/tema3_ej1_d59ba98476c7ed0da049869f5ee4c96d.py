# completa el código de la función
def suma_divisores(a):
    primo = False
    divisores = []

    for c in range(1, a-1):
        b = a % c
        if b == 0:
            divisores.append(c)
    Sumar = sum(divisores)
    if a == 1:
        Sumar = 0
    if Sumar == 1:
        primo = True
    return (Sumar, primo)