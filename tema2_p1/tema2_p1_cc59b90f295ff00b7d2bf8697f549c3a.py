# por favor escribe aquí tu función

def es_primo(num):
  if num == 1 or num == 2:     
    return False
  else:  
    for i in range(2, num):  
      if num % i == 0:    
        return False 
    return True
           