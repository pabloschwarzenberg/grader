# completa  código de la función
def suma_divisores(a):
  divisor=1
  suma_de_divisores=0
  primo=False
  for divisor in range (1,a):
    if a%divisor == 0:
      suma_de_divisores += divisor
      divisor += 1
  if suma_de_divisores == 1:
      primo=True
  return suma_de_divisores, primo
           