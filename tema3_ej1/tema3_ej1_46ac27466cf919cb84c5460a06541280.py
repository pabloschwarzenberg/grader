# completa el código de la función
def suma_divisores(a):
  Divisor = 2
  I = 0
  suma = 0
  while I < a:
    Numero = a / Divisor
    Numero2 = a // Divisor
    I += 1
    Divisor += 1
    if a == 1:
      primo = False
      break
    elif Numero == 1.0:
      primo =True
      break
    elif Numero == float(Numero2):
      primo = False
      break
  for divisor in range(1, a + 1):
      b = a / divisor
      c = a // divisor
      if a == 1:
          suma = 0
      elif b == float(c):
          suma += c
  if suma >= 1: 
    suma -= a
  return (suma,primo)
           