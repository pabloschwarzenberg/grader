def numero_perfecto(a):
    i=1
    b=0
    while i<a:
        if a%i==0:
            b=b+i
            i=i+1
        if a%i!=0:
            i=i+1

    if b==a:
        return True
    if b!=a:
        return False
