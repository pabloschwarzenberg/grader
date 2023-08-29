# completa el código de la función
def suma_divisores(a):
    i = 1
    b = 0
    while i < a:
        if a%i == 0:
            b = b + i
        i = i+1
    if b == 1:
        return b, True
    else:
        return b, False

           