# completa el código de la función
def amigos(a,b):
  Sumatoria_A = 0
  for divisor in range(1,a):
    if a%divisor == 0:
      Sumatoria_A = Sumatoria_A + divisor
  Sumatoria_B = 0
  for divisor in range(1,b):
    if b%divisor == 0:
      Sumatoria_B = Sumatoria_B + divisor
  if Sumatoria_A == b and Sumatoria_B == a:
    return True
  else: 
    return False