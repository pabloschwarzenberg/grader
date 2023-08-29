# completa el código de la función
def amigos(a,b):
    divisoresa=[]
    divisoresb=[]
    i=1
    o=1
    
    
    while i !=a :
        if a%i == 0:
            divisoresa.append(i)
        
        i+=1

    while o !=b :
        if b%o ==0:
            divisoresb.append(o)
        o+=1

    print(divisoresa)
    print(divisoresb)

    suma=0
    sumb=0
    for t in divisoresa:
        suma=suma+ t

    for y in divisoresb:
        sumb=sumb+ y
        
    if suma==b and sumb==a:
        return True
    else:
        return False



