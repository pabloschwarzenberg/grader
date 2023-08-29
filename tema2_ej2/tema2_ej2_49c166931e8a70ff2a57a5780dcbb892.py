# completa el código de la función
def divisores(n):
    f=n
    div=[]
    while n!=0:
        d=f%n
        n=n-1
        if d==0:
            div.append(n+1)
    return div
def amigos(a,b):
    d=len(divisores(a))
    e=len(divisores(b))
    s1=divisores(a)[d-1]
    s2=divisores(b)[e-1]
    while d!=1:
        s1=s1+divisores(a)[d-2]
        d=d-1
    while e!=1:
        s2=s2+divisores(b)[e-2]
        e=e-1
    if s1-a==b and s2-b==a:
        return True
    else:
        return False
           