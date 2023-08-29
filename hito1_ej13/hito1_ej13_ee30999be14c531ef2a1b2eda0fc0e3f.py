#Factores Primos
def esPrimo(numero):
  if numero==1:
    return False
  raizTruncada=int(numero**0.5)
  for divisores in range(2,raizTruncada+1):
    if numero%divisores==0:
      return False
  return True
def factoresPrimos(numero):
  for numeros in range(1,numero+1):
    if esPrimo(numeros) and numero%numeros==0:
      print(numeros)
numero=int(input())
factoresPrimos(numero)