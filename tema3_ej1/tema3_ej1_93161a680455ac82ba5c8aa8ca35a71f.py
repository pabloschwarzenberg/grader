# completa el código de la función
def suma_divisores(a):
    b = 1
    div = 0
    while b < a:
        if a % b == 0:
            div += b
        b += 1
    if div == 1:
        return div, True
    else:
        return div, False