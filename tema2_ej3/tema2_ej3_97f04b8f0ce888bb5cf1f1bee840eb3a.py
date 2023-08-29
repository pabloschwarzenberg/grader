def numero_perfecto(a):
  Suma = 0
  for divisor in range (1,a):
    if a%divisor == 0:
      Suma = Suma + divisor
  if Suma == a:
    return True
  return False           