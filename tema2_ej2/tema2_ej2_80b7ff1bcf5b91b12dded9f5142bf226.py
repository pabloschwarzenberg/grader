# completa el código de la función
def amigos(a,b):
    x=0
    y=0
    if a==b:
        return False
    for i in range (1, a+1):
        if a%i==0:
            x=x+i
    for i in range (1, b+1):
        if b%i==0:
            y=y+i
    if x==y:
        return True
    else:
        return False