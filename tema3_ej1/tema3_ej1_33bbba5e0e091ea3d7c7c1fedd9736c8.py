# completa el código de la función

def suma_divisores(a):
    suma = 0
    divisores = []
    for i in range(1,a):
        if (a % (i)) == 0:
            divisores.append(i)
    for i in divisores:
        suma = suma + i
    if suma == 1:
        primo = True
    else:
        primo = False
    return suma,primo