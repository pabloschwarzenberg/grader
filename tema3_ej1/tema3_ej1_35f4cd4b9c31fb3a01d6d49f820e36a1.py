# completa el código de la función
def suma_divisores(a):
  sum = 0
  div = a
  while div > 1:
    div = div - 1
    if (a % div) == 0:
        sum += div
  return sum