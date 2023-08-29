# completa el código de la función
def amigos(a,b):
    global e
    e = 0
    global d
    d = 0
    for i in range(1,a):
        if (a%i == 0):
            d=d+i
    for j in range(1,b):
        if (b%j == 0):
            e=e+j
    if (d == b) and (e == a):
        return True
    else:
        return False
           