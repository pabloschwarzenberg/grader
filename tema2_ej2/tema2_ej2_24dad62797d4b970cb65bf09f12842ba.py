# completa el código de la función
def amigos(a,b):
    suma1 = 0
    suma2 = 0
    for x in range(1,a):
        if a%x == 0:
            suma1 += x
    for y in range(1,b):
        if b % y == 0:
            suma2+=y
    if suma1 == b and suma2 == a:
        return True
    else:
        return False   