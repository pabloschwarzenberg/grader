# por favor escribe aquí tu función
import math
 
def es_primo(a):
    
    if a<=1:
        return False
 
    for x in range(2, math.ceil(math.sqrt(a))+1):
        if(a%x==0) and (x!=a):
            return False
        
    return True
       