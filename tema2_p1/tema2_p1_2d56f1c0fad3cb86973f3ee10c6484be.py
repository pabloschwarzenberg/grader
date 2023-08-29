# por favor escribe aquí tu función
def es_primo(numero):
  d=2
  primo=True
  while d<numero:
    if numero%d==0:
        primo=False
        break
    d=d+1
  if primo and 1<numero:
    return True
  else:
    return False