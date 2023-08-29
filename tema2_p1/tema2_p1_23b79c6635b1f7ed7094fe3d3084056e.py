# por favor escribe aquí tu función
def es_primo(numero):
  ndivisores = 0
  if numero == 2:
    return True
    
  else:
    for i in range (numero):
      if numero % (i+1) == 0:
        ndivisores +=1
        
        if i == (i+1):
          ndivisores +=1
          break
    
    if ndivisores == 2:
      return True
    
    if ndivisores != 2:
      return False
