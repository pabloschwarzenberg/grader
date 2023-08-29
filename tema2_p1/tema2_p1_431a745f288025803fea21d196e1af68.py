def es_primo(numero):
  y=numero
  if y==1:
    return False
  if y!=1:
    for i in range(2,y):
      n=y%i
      if n==0:
        return False
  return True
numero=67
es_primo(numero)