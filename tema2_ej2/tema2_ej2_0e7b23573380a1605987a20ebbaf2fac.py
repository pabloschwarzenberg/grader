# completa el código de la función
def amigos(a,b):
    suma1 = 0
    suma2 = 0
    for x in range (1, a - 1):
        if a % x == 0:
            suma1 = suma1 + x
    for n in range(1, b - 1):
        if b % n == 0:
            suma2 = suma2 + n
    if a == suma2 and b == suma1:
        return True
    else:
        return False