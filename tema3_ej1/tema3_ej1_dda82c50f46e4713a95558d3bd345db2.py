# completa el código de la función
def suma_divisores(a):
  div = 0
  for i in range(1,a-1):
    if a%i == 0:
      div = div + i
  if div == 1:
    return (div, True)
  else:
    return (div, False)
           