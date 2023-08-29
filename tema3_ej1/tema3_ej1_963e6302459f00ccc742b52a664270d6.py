# completa el código de la función
esprimo=False
numero=4
suma=0
def suma_divisores(a):
    acum=0
    for i in range(1,a,1):
        x=a%i
        if x==0 and i!=a:
            acum += i
    if acum == 1:
        return acum,True
    else:
        return acum, False