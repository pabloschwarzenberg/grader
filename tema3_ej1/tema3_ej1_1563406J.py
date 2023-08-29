# completa el código de la función
def suma_divisores(a):
    x=0
    for i in range(1,a):
        if a%i==0:
            x=x+i
    if x==1:
        return x,True
    else:
        return x,False