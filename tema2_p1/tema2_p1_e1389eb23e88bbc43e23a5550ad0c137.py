# por favor escribe aquí tu función
def es_primo(numero):
  if numero==1:
    return False
  for k in range(2,numero):
    if(numero%k)==0:
      return False
    else:
      return True
           