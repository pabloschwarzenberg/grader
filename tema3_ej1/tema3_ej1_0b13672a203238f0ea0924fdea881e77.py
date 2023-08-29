# completa el código de la función
def suma_divisores(a):
  SUMA = 0
  for i in range(1 , a-1):
    RESTO = a % i
    if RESTO != 0:
      continue
    SUMA += 1
  if SUMA == 1:
    numprimo = 1
  else:
    numprimo = 0
  
  return SUMA, numprimo
           