def es_primo(numero):
  primo=True
  if numero==1:
    primo=False
  i=2
  while i<=(numero/i):
    if numero%i==0:
      primo=False
      break
    i=i+1
  return primo