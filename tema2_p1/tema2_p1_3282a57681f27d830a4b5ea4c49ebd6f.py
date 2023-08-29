# por favor escribe aquí tu función
def es_primo(numero):
  count=0
  for x in range(1,numero+1):
    if numero%x ==0:
      count=count+1
  if count==2:
    return True
  else:
    return False       