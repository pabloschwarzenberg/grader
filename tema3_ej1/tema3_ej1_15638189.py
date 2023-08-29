# completa el código de la función
def suma_divisores(a):
    d=0
    for i in range(a):
        if (a%(i+1))==0:
            d=d+i+1
            continue
        else:
            continue
    d=d-a
    if d==1:
        return d,(2==2)
    else:
        return d,(2==1)