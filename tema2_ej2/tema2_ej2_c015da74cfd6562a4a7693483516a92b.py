# completa el código de la función
def amigos(a,b):
    lista1=[]
    lista2=[]
    acum1=0
    acum2=0
    amigo=0
    
    for i in range(1,a):
        if a%i==0:
            lista1.append(i)

    for i in range(1,b):
            if b%i==0:
                lista2.append(i)
            
    for e in lista1:
        acum1+=e

    for x in lista2:
        acum2+=x

    if acum1==b and acum2==a:
        amigo=True

    else:
        amigo=False
                
            
    return amigo