# completa el código de la función
def amigos(a,b):
    d = 2
    lista=[]
    while d<a:
        if a%d==0:
            lista.append(d)
        d=d+1
    d1 = 2
    lista2=[]
    while d1<b:
        if b%d1==0:
            lista2.append(d1)
        d1=d1+1
    c=sum(lista)+a
    d=sum(lista2)+b
    if c==d and a!=b:
        amigos=True
    else:
        amigos=False
    if b >= 1 and a >= 1:
        return amigos
           