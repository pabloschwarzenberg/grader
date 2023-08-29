def amigos(a,b):
    r=0
    i=1
    suma=0
    while i<a:
        if a%i==0:
            suma=suma+i
        i=i+1
    i=1
    rb=0
    sumab=0
    while i<b:
        if b%i==0:
            sumab=sumab+i
        i=i+1
    if suma==b and sumab==a:
        return True
    else:
        return False