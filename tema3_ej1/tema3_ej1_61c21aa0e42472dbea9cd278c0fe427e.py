# completa el código de la función
def suma_divisores(a):            
    s = 0                         
    if a == 1:                    
        return (0, False)         
    for i in range(1,a):          
        if a % i == 0:            
            s += i                
    if s != 1:                    
        return(s, False)          
    if s == 1:                    
        return (s, True)          