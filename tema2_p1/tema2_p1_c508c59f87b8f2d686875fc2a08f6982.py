# por favor escribe aquí tu función
def es_primo(numero):
  d=numero%2
  e=numero%3
  f=numero%4
  g=numero%5
  if numero==3 or numero==2:
    return True
  if numero==1:
    return False
  if d==0 or e==0 or f==0 or g==0:
    return False
  else:
    return True
           