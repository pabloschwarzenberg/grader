# completa el código de la función
def suma_divisores(a):
    a=int(a)
    x=0
    b=1
    while b<a:
        if a%b==0:
            x=x+b
        b=b+1
    if x==1:
        return x,True
    else:
        return x,False