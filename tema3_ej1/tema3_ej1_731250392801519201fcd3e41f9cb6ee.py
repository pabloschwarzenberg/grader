                 # completa el código de la función
def suma_divisores(a):
    
    s=0
    
    for i in range(1,a):
        
        if a%i==0:
            
            
            s=s+i
            
    if s==1:

            t= True
    else:
                  
            t= False
    return (s,t)        