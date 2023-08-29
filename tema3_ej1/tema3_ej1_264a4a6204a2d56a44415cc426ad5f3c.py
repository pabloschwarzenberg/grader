# completa el código de la función
def suma_divisores(a):
    contador= 0
    i = 1
    acumulador = 0
    while i < a:
        if a % i == 0:
            acumulador = acumulador + i
        i = i + 1

    for bar in range(1, acumulador+1):
        if(acumulador % bar == 0):
            contador += 1
    if(contador == 2):
        return acumulador, False
    else:
        if(a == 1):
            return acumulador, False
        else:
            return acumulador, True