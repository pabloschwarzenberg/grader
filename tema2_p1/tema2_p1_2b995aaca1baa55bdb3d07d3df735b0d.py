# por favor escribe aquí tu función
def es_primo(numero):
  if numero==1:
    return False
  elif numero==2:
    return True
  else:
    i=2
    while i<numero:
      if numero%i==0:
        return False
      else: 
        i=i+1
    return True
           