# por favor escribe aquí tu función
def es_primo(n):
    if n<=1:
        return False
    d=0
    c=1
    while d!=2:
        if n%c==0:
            d=d+1
            c=c+1
            #print(d)
            #print(c)
        else:
            c=c+1
            #print(c)
    c=c-1
    if c==n:
        return True
    elif c!=n:
        return False
           