# completa el código de la función
def suma_divisores(a):
  Suma = 0
  if a == 1:
    return (0,False)
  for divisor in range(1,a):
    if a%divisor == 0:
      Suma = Suma + divisor
  for divisor in range(2,a):
    if a%divisor == 0:
      return (Suma,False) 
  return (Suma,True) 
      