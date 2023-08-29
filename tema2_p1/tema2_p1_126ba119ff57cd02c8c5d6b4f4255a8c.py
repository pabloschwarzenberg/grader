# por favor escribe aquí tu función
def es_primo(numero):
  m=numero
  if m==1:
    return False
  if m!=1:
    for i in range(2,m):
      n=m%i
      if n==0:
        return False
  return True       
numero=67
es_primo(numero)