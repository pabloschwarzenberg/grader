# por favor escribe aquí tu función
def es_primo(numero):
  contador=0
  for i in range(1,numero+1):
    if numero%i==0:
      contador+=1
  if contador==2:
     return True
  else:
    return False
           