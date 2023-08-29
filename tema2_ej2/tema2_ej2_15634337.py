# completa el código de la función
def amigos(a,b):
    c=0
    d=0
    for i in range(1,a):
        if a%i==0:
            c=c+i
    if b==c:
        return True
    for i in range(1,b):
        if b%i==0:
            d=d+i
    if a==c:
        return True
    else:
        return False
           