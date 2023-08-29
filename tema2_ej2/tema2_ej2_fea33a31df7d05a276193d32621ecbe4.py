# completa el código de la función
def amigos(a,b):
    resul_a=[]
    n=1
    while n<a:
        if a%n==0:
            resul_a.append(n)
        n=n+1
    n=1
    resul_b=[]
    while n<b:
        if b%n==0:
            resul_b.append(n)
        n=n+1
    suma_a=0
    resul_a.append(a)
    resul_b.append(b)
    for i in (resul_a):
        suma_a=suma_a+i
        i=i+1
    suma_b=0
    for i in (resul_b):
        suma_b=suma_b+i
        i=i+1
    if a==b:
        return False
    if suma_a==suma_b:
        return True
    else:
        return False

           