# completa el código de la función
def amigos(a,b):
    inicio=1
    z=0
    if a==b or b==a and (a==1 or a==2 and b==1 or b==2):
        return(False)
    while inicio<=a:
        if a%inicio==0:
            z+=inicio
        inicio+=1
    inicio_f=1
    x=0
    while inicio_f<=b:
        if b%inicio_f==0:
            x+=inicio_f
        inicio_f+=1
    if x==z:
        return(True)
    else:
        return(False)