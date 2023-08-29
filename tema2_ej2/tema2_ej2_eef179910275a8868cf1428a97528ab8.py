# completa el código de la función
def amigos(a,b):
    suma=0
    a1=False
    b1=False
    for i in range(1,a):
        if a%i==0:
            suma+=i
    if suma==b:
        a1=True
    suma=0
    for i in range(1,b):
        if b%i==0:
            suma+=i
    if suma==a:
        b1=True
    if a1 and b1:
        return True
    else:
        return False  