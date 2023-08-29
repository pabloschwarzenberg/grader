# completa el código de la función
def suma_divisores(a):
    Sumita = 0
    for p in range(1, a):
        R = a % p
        if R == 0:
            Sumita = Sumita + p
    if Sumita == 1:
        primo = 1
    else:
        primo = 0

    return Sumita, primo