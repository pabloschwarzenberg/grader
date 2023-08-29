# completa el código de la función
def suma_divisores(a):
    i = 1
    divisores = 0
    while i < a:
        if a % i == 0:
            divisores += i
        i += 1
    if divisores == 1:
        return divisores, True
    else:
        return divisores, False