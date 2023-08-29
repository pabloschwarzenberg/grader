# completa el código de la función
def suma_divisores(a):
    if a==1:
        return 0,False
    i=1
    contador=0
    while i<a:
        x=a%i
        if x==0:
            contador=contador+i
        else:
            pass
        i = i + 1
    if contador==1:
        return contador,True
    else:
        return contador,False
