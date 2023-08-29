# completa el código de la función
def amigos(a,b):
    suma1 = 0
    suma2 = 0
    for x in range(1,a):
        if (a % x) == 0:
            suma1 += x
    if suma1 != b:
        return(False)
    for d in range(1,b):
        if (b % d) == 0:
            suma2 += d
    if suma2 != a:
        return(False)
    return(True)

