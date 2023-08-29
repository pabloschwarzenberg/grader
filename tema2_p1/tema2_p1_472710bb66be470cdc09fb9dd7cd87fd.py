def es_primo(funcion):
    
    if funcion < 2:
         
         return False
        
    for i in range(2, funcion):
        
         if funcion % i == 0:
             
               return False

    return True   

           