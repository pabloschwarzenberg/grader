def numero_perfecto(a):
    n=0
    for x in range(1,a):
        if a%x==0:
            n=n+x
    if a==n:
        return True
    else:
        return False

