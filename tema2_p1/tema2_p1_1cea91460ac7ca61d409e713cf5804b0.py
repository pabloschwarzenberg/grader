# por favor escribe aquí tu función
def es_primo(numero):
  div=1
  numdiv=0
  while div<=numero:
    if numero%div==0:
      numdiv+=1
    div+=1
  if numdiv==2:
    return True
  else:
    return False
    
           