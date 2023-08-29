# completa el código de la función
def suma_divisores(a):
  divisores = []
  for x in range(1, a):
    if a%x == 0:
      divisores.append(x)
  y = sum(divisores)
  if y == 1:
    valor = True
  else:
    valor = False
  return y, valor