# completa el código de la función
def suma_divisores(a):
  y = 0
  primo = False
  for x in range(1,a):
    if a%x == 0:
      y += x
  if y == 1:
    primo = True
  return y , primo
           