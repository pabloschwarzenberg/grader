# completa el código de la función
def amigos(a,b):
    f = 0
    c = 0
    for n in range(1, a):
        if a % n == 0:
            c = c+n
    for e in range(1, b):
        if b % e == 0:
            f = f+e
    if c == b and f == a and a != b:
        return True
    else:
        return False