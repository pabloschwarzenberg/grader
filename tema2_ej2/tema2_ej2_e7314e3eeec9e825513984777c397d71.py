# completa el código de la función
def amigos(a,b):
    if a==b:
        return False
    i1=1
    x=1
    suma1 = 0
    suma2 = 0
    while i1<a:
        if a%i1==0:
            suma1=suma1+i1
        i1=i1+1
    while x<b:
        if b%x==0:
            suma2=suma2+x
        x=x+1
    if suma1==b and suma2==a:
        return True
    if not suma1==b and suma2==a:
        return False





           