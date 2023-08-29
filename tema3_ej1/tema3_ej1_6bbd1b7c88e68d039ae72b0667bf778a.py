# completa el código de la función
def suma_divisores(a):
    Suma = 0
    for p in range(1, a):
        R = a % p
        if R == 0:
            Suma = Suma + p
    if Suma == 1:
        primo = 1
    else:
        primo = 0

    return Suma, primo   