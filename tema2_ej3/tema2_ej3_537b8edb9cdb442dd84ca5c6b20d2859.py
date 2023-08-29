def numero_perfecto(a):
    w=int(a)
    r=[]
    d=1
    while w>d:
        if w%d==0:
            r.append(d)
        d=d+1
    if sum(r)==w:
        return True
    else:
        return False