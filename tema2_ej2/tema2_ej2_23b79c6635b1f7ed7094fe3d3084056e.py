# completa el código de la función
def amigos(a,b):
    sumadivisoresa = 0
    sumadivisoresb = 0
    
    for i in range (a):
        if (i+1) == a:
            break
        
        if a % (i+1) == 0:
            sumadivisoresa += (i+1)
      
    for i in range(b):
        if (i+1) == b:
            break
        
        if b % (i+1) == 0:
            sumadivisoresb += (i+1)
            
    if sumadivisoresa == b and sumadivisoresb == a:
        return True
    
    return False
       