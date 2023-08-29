def suma_divisores(n):
    
    divisores=[0]
    
    
    for i in range(1,n,1):
        print("cuando i es ",i, "=",n%i)

        if(n%i==0):
            divisores.append(i)            
            
    
    suma=(sum(divisores))        
    primo=[0]       
    
    print(suma)        
    for i in range(1,suma,1):
        print("cuando j es ",i, "=",suma%i)
  
        if(suma%i==0):
            primo.append(i)
            
    
    if(suma==1):
        return suma,True
    else:
        return suma,False