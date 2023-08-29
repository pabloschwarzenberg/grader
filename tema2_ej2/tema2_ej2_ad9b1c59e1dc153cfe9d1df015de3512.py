def suma_divisores(x):
    suma = 0
    numero = 1
    while numero <= (x//2)+1:
        if x%numero == 0:
            suma = suma + numero
        numero += 1
    return suma
def amigos(x,y):
    if x==y:
        return False
    if (suma_divisores(x) == y) and (suma_divisores(y) == x):
        return True
    return False
           