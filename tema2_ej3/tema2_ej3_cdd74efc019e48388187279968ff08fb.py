def numero_perfecto(a):
    c=1
    s=0
    while c!=a:
        if a%c==0:
            s=s+c
        c=c+1
    if s==a:
        return True
    else:
        return False
    