def buscarTodas(a,b):
    posicion = ""   
    for i in range(0,len(a)):
        if a[i] == b:
          if i == 0:
               posicion = posicion +str(i)
          else:
               posicion = posicion + " " +str(i)
                
            
    return posicion
    
            
    


        
    
    