# completa el código de la función
def suma_divisores(a):
  contador=0
  EsPrimo=False
  for i in range (1,a):
    if a % i == 0:
      contador = contador + i
      if contador == 1:
        EsPrimo=True
      if contador != 1:
        EsPrimo=False
  return contador,EsPrimo