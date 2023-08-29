def amigos(a,b):
    x=1
    y=0
    while x!=a:
        if a%x==0:
            y=y+x
        x=x+1
    w=1
    v=0
    while w!=b:
        if b%w==0:
            v=v+w
        w=w+1
    return v==a and y==b
