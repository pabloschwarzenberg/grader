# completa el código de la función
def suma_divisores(a):
    n = 0
    prm = False
    for i in range(1, a):
        if a % i == 0:
            n = n + i
    if n == 1:
        prm = True
    return n, prm
