# completa el código de la función
def suma_divisores(a):
    divisores = 0
    p = 1
    while p < a:
        if a//p == a/p and p != 0:
            divisores = divisores + p
        p += 1
    return divisores, bool(1 == divisores)