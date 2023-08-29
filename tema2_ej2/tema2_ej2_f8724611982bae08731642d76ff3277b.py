# completa el código de la función
def amigos(n,m):
    divisor=1
    c=0
    b=0
    x=1
    while divisor<n:
        if n%divisor==0:
            c=c+divisor
        divisor=divisor+1
    while x<m:
        if m%x==0:
            b=b+x
        x=x+1
    if b==n and c==m:
        return(True)
    else:
        return(False)
           