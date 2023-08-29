# completa el código de la función
def amigos(a,b):
    n=1
    lista_a=[]
    while n<a:
        if a%n==0:
            lista_a.append(n)
        n=n+1
        lista_a.sort()
    p=1
    lista_b=[]
    while p<b:
        if b%p==0:
            lista_b.append(p)
        p=p+1
        lista_b.sort()
    s_a=0
    for i in (lista_a):
        s_a=s_a+i
    s_b=0
    for i in (lista_b):
        s_b=s_b+i
    if s_a==b and s_b==a:
        return True
    else:
        return False