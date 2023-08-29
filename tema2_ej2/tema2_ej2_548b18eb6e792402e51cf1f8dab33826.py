def amigos(a,b):
    
    listaA = []
    listaB = []
    
    for i in range (1,a):
        if a%i == 0:
            listaA.append(i)

    for i in range (1,b):
        if b%i == 0:
            listaB.append(i)

    sumaA = sum(listaA)
    sumaB = sum(listaB)
        

    if sumaA == b and sumaB == a:
        return True
    else:
        return False