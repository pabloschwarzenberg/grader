# completa el código de la función
def suma_divisores(a):
    divisores = []
    for x in range(1,a):
        if a % x == 0:
            divisores.append(x)
    suma = 0
    for y in divisores:
        suma = suma + y

    primo = True
    if suma < 1:
        primo = False
    elif suma == 2:
        primo = True
    elif suma % 2 == 0:
        primo = False

    lim = int(round((suma)**(1/2)))

    i = 3
    while i <= lim:
        if suma % i == 0:
            primo = False
        i = i + 3
    return suma,primo
           