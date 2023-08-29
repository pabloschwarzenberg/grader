def es_primo(numero):
  if numero==1:
    return False
  for rango in range(2,numero):
    if numero%rango ==0:
      return False
    else:
      return True