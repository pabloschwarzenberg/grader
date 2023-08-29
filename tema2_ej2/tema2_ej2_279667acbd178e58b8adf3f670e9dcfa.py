# completa el código de la función
def amigos(a,b):
    lista_a = 0
    for x in range(1,a):
        if a % x == 0:
            lista_a += x
    lista_b = 0
    for y in range(1,b):
        if b % y == 0:
            lista_b += y
    if lista_a == b and lista_b == a:
        return True
    return False
           