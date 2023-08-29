def numero_perfecto(a):
    c=0
    for x in range(1,a):
        if a%x == 0:
            c=c+x
    if c==a:
        return True
    else:
        return False
