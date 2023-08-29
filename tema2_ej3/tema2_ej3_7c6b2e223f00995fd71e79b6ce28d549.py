def numero_perfecto(a):
    i=1
    suma=0
    perfecto=False
    while i<a:
        if a%i==0:
            suma+=i
            i=i+1
        else:
            i=i+1
            
        
    if suma==a:
        perfecto=True
    
    return perfecto


