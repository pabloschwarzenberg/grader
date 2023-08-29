# completa el código de la función
def suma_divisores(a):
    suma = 0
    esPrimo = False
    primos = []
    for x in range(1,a):
        if a%x == 0 :
            suma += x
    for x in range(2,a):
        if a%x == 0 :
            return suma,False
    if a == 1 :
        return suma,False
    return suma,True