# completa el código de la función
def amigos(a,b):
    n=0
    m=0
    i=a
    while i>0:
        if a%i==0:
            n=i+n
        i=i-1
    n=n-a
    l=b
    while l>0:
        if b%l==0:
            m=l+m
        l=l-1
    m=m-b
    if n==b and m==a:
        return True
    else:
        return False

