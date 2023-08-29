def suma_divisores(a):
    x=1
    y=0
    while x!=a:
        if a%x==0:
            y=y+x
        x=x+1
   
    return y, y==1