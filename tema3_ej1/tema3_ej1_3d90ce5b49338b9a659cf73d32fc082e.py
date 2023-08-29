# completa el código de la función
def suma_divisores(a):
    sumDiv = 0
    for i in range(a):
        if i != 0 and a % i == 0:
            sumDiv += i
    cont = 0

    if sumDiv == 1:
        return sumDiv, True
    else:
        return sumDiv, False
           