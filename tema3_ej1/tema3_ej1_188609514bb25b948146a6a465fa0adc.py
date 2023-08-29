# completa el código de la función
def suma_divisores(a):
    suma = 0
    i = 1
    while i <= (a//2):
        if a%i == 0:
            suma += i
        i += 1
    if suma == 1:
        p = True
    else:
        p = False

    return suma,p
           