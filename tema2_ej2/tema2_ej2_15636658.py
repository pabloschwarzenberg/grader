# completa el código de la función
def amigos(a,b):
    k=a
    suma=0
    for i in range (a-1):
        if a==1:
            suma=1
        elif a%k==0:
            suma+=a//k
        k=k-1
    l=b
    sumdiv=0
    for i in range (b-1):
        if b==1:
            sumdiv=1
        elif b%l==0:
            sumdiv+=b//l
        l=l-1
    
    if suma==b and sumdiv==a:
        return True
    else:
        return False