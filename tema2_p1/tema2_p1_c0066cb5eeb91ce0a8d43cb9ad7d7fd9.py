# por favor escribe aquí tu función
def es_primo(numero):
  if numero==1:
    return False
  for p in (2,numero):
    if numero%p == 0: 
      return False
    elif numero%p!=0:
      return True

           