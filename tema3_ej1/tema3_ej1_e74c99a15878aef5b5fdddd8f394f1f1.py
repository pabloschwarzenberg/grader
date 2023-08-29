def suma_divisores(a):
    primo=False
    s=0
    d=1
    while d<a:
        if a%d==0:
            s=s+d
        d=d+1
    if s==1:
        primo=True
    return s,primo
