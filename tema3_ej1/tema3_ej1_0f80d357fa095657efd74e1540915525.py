# completa el código de la función
def suma_divisores(a):
    Primo = False
    Divisores = []

    for c in range(1, a - 1):
        b = a % c
        if b == 0:
            Divisores.append(c)
    Sumar = sum(Divisores)
    if a == 1:
        Sumar = 0
    if Sumar == 1:
        Primo = True
    return (Sumar, Primo)