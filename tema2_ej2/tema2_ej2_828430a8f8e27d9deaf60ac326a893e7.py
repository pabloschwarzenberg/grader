# completa el código de la función
def amigos(a,b):
    x=1
    y=1
    estado = False
    for i in range(2, a):
        if (a % i == 0):
            x = x + i
    for i in range(2, b):
        if (b % i == 0):
            y = y + i
    if b == x and a == y:
        estado = True
    else:
        estado = False
    return estado