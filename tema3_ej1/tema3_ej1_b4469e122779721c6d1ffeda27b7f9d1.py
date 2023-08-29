# completa el código de la función
def suma_divisores(x):
    z = 0
    for w in range(1,x):
        if x % w == 0:
            z = z + w

    y = True
    if x <=1:
        y = False
    elif x == 2 :
        y = True
    else:
        for w in range(2, x):
            if x % w == 0:
                y = False

    return (z,y)
