def numero_perfecto(a):
    d=[]
    i=2
    while 2<=i<=a:
        b=a/i
        if a%i==0:
            d.append(b)
        i=i+1
    z=sum(d[:])
    if z==a:
        return True
    if z!=a:
        return False