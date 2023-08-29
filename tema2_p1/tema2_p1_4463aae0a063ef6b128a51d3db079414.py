# por favor escribe aquí tu función
def es_primo(numero):
  k=0
  for i in range(numero):
    if(numero%(i+1)==0):
      k+=1
  if(k==2):
    return True
  else:
    return False
           