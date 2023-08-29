# completa el código de la función
def suma_divisores(a):
    x = 1
    y = 0
    c = 0
    if a == 1:
        return (0, False)
    while x < a:
        if a % x == 0:
            y = y + int(x)
            c += 1
        x += 1
    if c == 1:
        return (y, True) 
    else:
        return (y, False)
           