# completa el código de la función
def amigos(a,b):
    al=[]
    bl=[]
    c=1
    d=1
    while c<=a:
        if a%c==0:
            al.append(c)
            c=c+1
        else:
            c=c+1
    while d<=b:
        if b%d==0:
            bl.append(d)
            d=d+1
        else:
            d=d+1
    if sum(al)==sum(bl) and a!=b:
        return True
    else:
        return False
    