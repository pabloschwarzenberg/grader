# completa el código de la función
def suma_divisores(a):
    c=0
    for x in range(1,a):
        if a%x == 0:
            c=c+x
    if c == 1:
        return c,True
    else:
        return c,False

           