# por favor escribe aquí tu función
def es_primo(numero):
  y = 0
  primo = False
  for x in range(1,numero):
    if numero%x == 0:
      y += x
  if y == 1:
    primo = True
  return primo
           