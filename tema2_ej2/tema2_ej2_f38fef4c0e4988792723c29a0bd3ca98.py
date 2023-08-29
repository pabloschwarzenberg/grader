# completa el código de la función
def amigos(a,b):
    d=[]
    for i in range(1,a):
        if a%i==0:
            d.append(i)
    n=0
    for i in d:
        n=n+i
    if n==b:
        return True
    else:
        return False

