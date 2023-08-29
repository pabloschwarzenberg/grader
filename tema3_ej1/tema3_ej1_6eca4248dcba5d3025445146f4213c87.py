# completa el código de la función

def suma_divisores(a):
    d=[]
    i=2
    while 2<=i<=a:
        b=a/i
        if a%i==0:
            d.append(b)
        i=i+1
    z=sum(d[:])
    
    if z==1:
        return (int(z),True)
    if z!=1:
        return (int(z),False)