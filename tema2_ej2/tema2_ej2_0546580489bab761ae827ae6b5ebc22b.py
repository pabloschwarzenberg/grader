# completa el código de la función
def amigos(a, b):
    suma = 0
    sumb = 0
    for x in range(1, a):
        if a % x == 0:
            suma += x
    for x in range(1, b):
        if b % x == 0:
            sumb += x
    if suma == b and sumb == a:
        return True
    else:
        return False

