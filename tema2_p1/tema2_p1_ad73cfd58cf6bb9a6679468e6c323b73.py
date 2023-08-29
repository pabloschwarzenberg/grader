# por favor escribe aquí tu función
import math 

def es_primo(x):
    if x<=1:
        return False
    
    for y in range (2 , math.ceil(math.sqrt(x))+1):
                    if x%y==0 and y!=x:
                        return False
    return True
    
           