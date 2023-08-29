# completa el código de la función
def suma_divisores(a):
    sumas=0
    n=1
    if a==1:
        sumas=0
    while n<a:
        if a%n==0:
            sumas=sumas+n
            n=n+1
        else:
            n=n+1
    if sumas==1:
        return sumas,True
    else:
        return sumas,False