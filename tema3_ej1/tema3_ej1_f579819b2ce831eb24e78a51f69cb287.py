# completa el código de la función
def suma_divisores(a):
    n = 0
    for i in range(1, a):
        if a % i == 0:
            n = n + i
        else:
            continue
    if n == 1:
        numero = True
    else:
        numero = False
    return (n, numero)