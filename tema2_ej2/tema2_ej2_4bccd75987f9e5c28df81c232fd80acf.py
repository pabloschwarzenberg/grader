# completa el código de la función
def amigos(a,b):
    listaA = []
    for i in range(1,a):
        if a % i == 0:
          listaA.append(i)
        
    listaB = []    
    for i in range(1,b):
        if b % i == 0:
          listaB.append(i)
     
    sumlisA= sum(listaA)
    sumlisB= sum(listaB)
    if sumlisA == b and sumlisB == a:
        return True
    else: return False
           