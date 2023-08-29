# completa el código de la función
def suma_divisores(a):
  divisor = 1
  suma_divisores = 0
  esPrimo = False
  
  while divisor < a:
    if a % divisor == 0:
      suma_divisores += divisor
    divisor += 1
  if suma_divisores == 1:
    esPrimo = True
  
  return (suma_divisores, esPrimo)
           