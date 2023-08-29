def numero_perfecto(a):
    i=1
    suma=0
   
    
    
    while i<a:
        if a%i==0:
            suma+=i
        else:
            pass
        i+=1
    if suma==a:
        perfectob=True
        
    else:
        perfectob=False

    return perfectob
           