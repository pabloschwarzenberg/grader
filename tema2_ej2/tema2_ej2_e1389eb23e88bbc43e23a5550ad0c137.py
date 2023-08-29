# completa el código de la función
def amigos(a,b):
    x=0
    r=0
    for k in range(1,a):
        if (a%k)==0:
            x=x+k
    if x==b:
        return True
    else:
        return False
    for i in range(1,b):
        if(b%k)==0:
            r=r+i
    if r==a:
        return True
    else:
        return False