def amigos(a,b):
    a1=0
    b1=0
    for x in range(1,a):
        if a%x==0:
            a1+=x
    for x in range(1,b):
        if b%x==0:
            b1+=x
    if b1==a and a1==b:
        return True
    else:
        return False