# completa el código de la función
def suma_divisores(a):
    a=int(a)
    n=1
    s=0
    while a!=n:
        if a%n==0:
            r=n
            s+=r
        else:
            n+=1
            continue
        n+=1
        continue
    if s==1:
        return s,True
    else:
        return s,False