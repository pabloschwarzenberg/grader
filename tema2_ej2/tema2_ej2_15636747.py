# completa el código de la función
def amigos(a,b):
    suma1=0
    suma2=0
    for i in range(1,int(a/2)+1):
        c=a%i
        if c==0:
            suma1=suma1+i
    for i in range(1,int(b/2)+1):
        d=b%i
        if d==0:
            suma2=suma2+i
    if suma1==b and suma2==a:  
        return True
    else:
        return False


           