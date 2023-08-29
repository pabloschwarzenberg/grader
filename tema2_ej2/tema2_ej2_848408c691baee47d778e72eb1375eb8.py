# completa el código de la función
def amigos(a,b):
    Chocolate = 0
    Menta = 0
    for i in range(1, a):
        if a % i == 0:
            Chocolate += i

    for x in range(1, b):
        if b % x == 0:
            Menta += x

    return Chocolate == b and Menta == a
           