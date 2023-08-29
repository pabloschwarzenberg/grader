# completa el código de la función
def suma_divisores(a):
    factores = []
    for x in range (1,a):
        if a % x == 0:
            factores.append(x)
    suma = 0
    for i in factores:
        suma = suma + i
    if suma == 1:
        return suma, True
    else:
        return suma, False