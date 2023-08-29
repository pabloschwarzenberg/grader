# por favor escribe aquí tu función
def es_primo(numero):
  primo = True
  if numero == 1:
    primo = False
  for i in range(2,numero):
    if numero%i == 0:
      primo = False
  return primo