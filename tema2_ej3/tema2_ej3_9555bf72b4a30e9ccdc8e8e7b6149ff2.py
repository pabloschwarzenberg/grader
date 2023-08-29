def numero_perfecto(a):
    sd=0
    for n in range(1,a):
        if a/n==a//n:
            sd+=n
    if sd==a:
        return True
    else:
        return False
           