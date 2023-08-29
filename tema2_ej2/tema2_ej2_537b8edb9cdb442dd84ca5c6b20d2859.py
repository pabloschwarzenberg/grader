def amigos(a,b):
    r=[]
    r2=[]
    d=1
    g=1
    while a>d:
       if a%d==0:
            r.append(d)
       d=d+1
    while b>g:
        if b%g==0:
            r2.append(g)
        g=g+1
    if sum(r)==b and sum(r2)==a:
        return True
    else:
        return False
        
           