def amigos(a,b):
    m = 0
    s = 0
    d = 0
    f = 0
    while m < a-1:
        m += 1
        if a%m==0:
            s += m
    while d < b-1:
        d += 1
        if a%d==0:
            f += d
    if s==f or (a==1 and b==2):
        return False
    else:
        return True