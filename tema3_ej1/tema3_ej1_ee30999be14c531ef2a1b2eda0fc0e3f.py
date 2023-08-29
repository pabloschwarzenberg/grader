# completa el código de la función
def esPrimo(a):
  if a==1:
    return False
  raizTruncada=int(a**0.5)
  for divisores in range(2,raizTruncada+1):
    if a%divisores==0:
      return False
  return True
def suma_divisores(a):
  numPrimo=esPrimo(a)
  suma=0
  for numeros in range(1,a):
    if a%numeros==0:
      suma+=numeros
  return (suma,numPrimo)
           