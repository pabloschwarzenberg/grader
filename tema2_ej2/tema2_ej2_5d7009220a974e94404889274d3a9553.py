def divisores(numero):
    resultado=[]
    n=2
    while n<numero:
        if numero%n == 0:
            resultado.append(n)
        n=n+1
    return resultado

def amigos(a,b):
   
    d1=divisores(a)
    d2=divisores(b)

    s=0
    d1=divisores(a)
    for i in d1:
        s=s+i

    suma1=s+1

    k=0
    d2=divisores(b)
    for i in d2:
        k=k+i

    suma2=k+1

    if suma1==b and suma2==a:
        return True
    else:
        return False

           