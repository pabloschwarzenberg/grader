# por favor escribe aquí tu función
def es_primo(numero):
  i = 0
  resto = numero%2
  if numero==0:
    return False
  if numero==1:
    return False
  if numero !=0:
    for var1 in range(2,numero):
        if resto == 0: 
            i = i + 1
    if i ==0:
      return True
    else:
      return False
   