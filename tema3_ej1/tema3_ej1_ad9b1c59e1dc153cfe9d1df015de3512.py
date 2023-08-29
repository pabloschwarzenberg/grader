# completa el código de la función
def suma_divisores(a):
    t=1
    r=0
    while t<a:
        if a%t==0:
            r=r+t
            t=t+1
        else:
            r=r
            t=t+1
    if r==1:
        return (r, True)
    elif r==0:
        return (r,False)
    elif r>1:
        return (r,False)



           