#suma de los divisores de un numero
def suma_divisores(x):
    s = 0
    for a in range(1,x):
        if x % a == 0:
            s = s +a

    b = True
    if x <=1:
        b = False
    elif x == 2:
        b = True
    else:
        for a in range(2, x):
            if x % a == 0:
                b = False

    return (s,b)