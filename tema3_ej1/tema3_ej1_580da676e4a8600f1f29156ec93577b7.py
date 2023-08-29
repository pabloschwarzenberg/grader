# completa el código de la función
def suma_divisores(x):
    
    d=[0]
    
    
    for a in range(1, x, 1):
        print("cuando a es ",a, "=",x % a)

        if(x % a == 0):
            d.append(a)            
            
    
    s=(sum(d))        
    p=[0]       
    
    print(s)        
    for a in range(1,s,1):
        print("cuando b es ",a, "=",s % a)
  
        if(s % a  == 0):
            p.append(a)
            
    if(s == 1):
        return s,True
    else:
        return s,False