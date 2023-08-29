# completa el código de la función
def amigos(a,b):
    i=1
    c=1
    acumA=0
    acumB=0
    valor=0
    while i<a:
        if a%i==0:
            acumA=acumA+i
        i=i+1    
    while c<b:
        if b%i==0:
            acumB=acumB+c
        c=c+1
    if (a==1 and b==2)or(a==2 and b==1):
        valor=False
    elif acumA==b:
        valor=True
    elif acumB==a:
        valor=True
    else:
        valor=False
    return valor
a=4
b=3
amigos(a,b)
print(amigos(a,b))
           