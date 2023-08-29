# completa el código de la función
def suma_divisores(z):
    q = 0
    for i in range(1,z):
        if z % i == 0:
            q = q + i

    P = True
    if z <=1:
        P = False
    elif z == 2 :
        P = True
    else:
        for i in range(2, z):
            if z % i == 0:
                P = False

    return (q,P)