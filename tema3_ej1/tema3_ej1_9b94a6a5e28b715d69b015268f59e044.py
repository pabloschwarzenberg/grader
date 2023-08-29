# completa el código de la función
def suma_divisores(dividendo):
  divisor = 0
  cociente = 0
  suma = 0
  retorno = False
  for i in range(dividendo):
    divisor = i+1
#asi valida divisores de dividendo
    if dividendo%divisor == 0 and divisor != dividendo:
      suma = divisor + suma
  if suma == 1:
    retorno = True

  return suma,retorno