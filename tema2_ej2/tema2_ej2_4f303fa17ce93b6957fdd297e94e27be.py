# completa el código de la función
def amigos(a,b):
    sumaa = -a
    sumab = -b
    for i in range(a):
        if a % (i+1) == 0:
            sumaa += (i+1)
    if sumaa == b:
        for i in range(b):
            if a % (i+1) == 0:
                sumab += (i+1)
        if sumab == a:
            return True
        else:
            return False
    else:
        return False         