def suma_divisores(a):
    i=1
    suma=0
    primo=0
   
    while i<a:
        if a%i==0:
            suma=suma+i
        else:
            pass
        i=i+1
        
        
        
    if suma==1:
        primo=True
    else:
        primo=False

    return suma,primo
        
        
    


        
        
