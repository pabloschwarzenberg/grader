# completa el código de la función
def amigos(a, b):
    amigo_1 = 0
    amigo_2 = 0
    for y in range(1, a):
        if a % y == 0:
            amigo_1 += y

    for x in range(1, b):
        if b % x == 0:
            amigo_2 += x
    return amigo_1 == b and amigo_2 == a