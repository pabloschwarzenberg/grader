# completa el código de la función
def suma_divisores(a):
    num = False
    suma = 0
    for i in range(a):
        if i == 0:
            continue
        elif a % i == 0:
            suma = suma + i
    if suma == 1:
        num = True
    return suma,num