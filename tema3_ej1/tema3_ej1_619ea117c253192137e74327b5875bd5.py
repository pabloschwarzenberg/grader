# completa el código de la función
def suma_divisores(a):
    l=[]
    y=0
    for x in range(1,a):
        if a % x ==0:
            y = y + x
            l.append(x)
    if len(l) == 1:
        x = True
    else:
        x = False
    return y, x
           