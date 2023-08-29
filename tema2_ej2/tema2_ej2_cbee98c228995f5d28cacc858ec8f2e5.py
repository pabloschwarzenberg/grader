# completa el código de la función
def amigos(a,b):
    i=1
    Divisores_A=[]
    Divisores_B=[]
    while i<a:
        if a%i==0:
            Divisores_A.append(i)
        i=i+1

    j=1
    while j<b:
        if b%j==0:
            Divisores_B.append(j)
        j=j+1

    x=0
    sumaA=0
    while x<(len(Divisores_A)):
        sumaA=Divisores_A[x]+sumaA
        x=x+1
    y=0
    sumaB=0
    while y<(len(Divisores_B)):
        sumaB=Divisores_B[y]+sumaB
        y=y+1
    if (sumaA==b)and(sumaB==a):
        return True
    else:
        return False     