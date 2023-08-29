# completa el código de la función
def amigos(a,b):
  divisor = 0
  divisorb = 0
  for i in range(1,a):
    resultado = a / i
    resultado2 = a // i
    if resultado == float(resultado2):
      if resultado2 == a:
        continue
      divisor += resultado2
  for i in range(1,b):
    resultado1 = b / i
    resultado3 = b // i
    if resultado1 == float(resultado3):
      if resultado3 == b:
        continue
      divisorb += resultado3
  if divisor == b - 1 and divisorb == a - 1:
    ab = True
  else:
    ab = False
  return ab