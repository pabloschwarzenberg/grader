# completa el código de la función
def suma_divisores(a):
    divisor = []
    
    for i in range(1,a):
        if a % i == 0:
            if a == i:
                divisor.append(0)
            else:
                divisor.append(i)
    
    variable = False
    if sum(divisor) >= 1:
        if sum(divisor) == 1 or sum(divisor) == 0:
            variable = True
        
            
            
    return(sum(divisor), variable)    
            
        
        
        
suma_divisores(13)      
