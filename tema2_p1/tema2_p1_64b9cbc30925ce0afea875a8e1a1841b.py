def es_primo(numero):
    i=2
    while i<numero: 
        if numero%i==0:
            return False
        else:
            i=i+1
    if numero==1:
      return False
    elif numero==2:
      return True
    else:
      return True
    
    
      
      
           