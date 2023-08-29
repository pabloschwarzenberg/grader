def es_primo(numero):
  if numero<2:
      return False
  for x in range(2,numero):
      if numero%x==0:
          return False
  return True  