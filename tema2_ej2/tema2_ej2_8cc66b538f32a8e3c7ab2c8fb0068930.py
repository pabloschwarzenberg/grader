# completa el código de la función
def amigos(a,b):
    c=0
    d=0
    for i in range(1,a):
        if a%i==0:
            c=c+i
    for n in range(1,b):
        if b%n==0:
            d=d+n
    if c==b and d==a:
        return True
    else:
        return False