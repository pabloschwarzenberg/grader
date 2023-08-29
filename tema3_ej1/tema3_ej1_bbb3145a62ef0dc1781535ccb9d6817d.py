# completa el código de la función
def suma_divisores(m):
    suma = 0
    for p in range(1,m):
        if m % p == 0:
            suma = suma + p

    x = True
    if m <=1:
        x = False
    elif m == 2 :
        x = True
    else:
        for p in range(2, m):
            if m % p == 0:
                x = False

    return (suma,x)
           