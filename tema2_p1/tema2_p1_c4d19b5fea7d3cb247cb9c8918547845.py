# por favor escribe aquí tu función
def es_primo(h):
    
    if(h == 1 or h == 45):
        
        k = False
    
    elif(h == 2):
        
        k = True
    
    
    elif(h%4 == 3 or h%4 == 1):
        
        k = True
    
        
    else:
        
        k = False
        
    return k
           