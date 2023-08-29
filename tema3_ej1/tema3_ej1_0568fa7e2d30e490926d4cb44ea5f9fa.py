# completa el código de la función
def suma_divisores(x):
    suma = 0
    for i in range(1,x):
        if x % i == 0:
            suma = suma + i

    y = True
    if x <=1:
        y = False
    elif x == 2 :
        y = True
    else:
        for i in range(2,x):
            if x % i == 0:
                y = False

    return (suma,y)