def amigos (a,b):
    listaA=[]
    listaB=[]
    for i in range(1,a):
        if a%i==0:
            listaA.append(i)
        suma=suma+i
    for i in range(1,b):
        if b%i==0:
            listaB.append(i)
        suma1=suma1+i
    if suma==b and suma1==a:
        return True
    else:
        return False



