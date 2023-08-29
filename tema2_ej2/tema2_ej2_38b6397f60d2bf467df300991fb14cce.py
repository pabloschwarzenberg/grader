# completa el código de la función
def amigos(a,b):
    x1=0
    y1=0
    for x in range(1,a):
        if a%x==0:
            x1+=x
    for x in range(1,b):
        if b%x==0:
            y1+=x
    if y1==a and x1==b:
        return True
    else:
        return False
           