def numero_perfecto(a):
    div=0
    i=1
    while i<=(a):
        p=a%i
        if p==0:
            div=div+i
        div=div
        i=i+1
    m=(div-a)
    if m==a and a!=0:
        return True
    else:
        return False
def suma_numeros_perfectos(n):
    t=1
    div=0
    k=0
    while t<=(n):
        w=n%t
        if w==0:
            div=div+t
        div=div
        if div==t:
            k=k+div
        k=k
        t=t+1
    if True:
        return k