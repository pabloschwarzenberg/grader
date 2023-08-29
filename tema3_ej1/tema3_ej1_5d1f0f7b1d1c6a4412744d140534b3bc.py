# completa el código de la función
def suma_divisores(n):
  divisores=[]
  for i in range(1,n):
    if n%i==0:
      i =divisores.append(i)
  suma=0
  for divisor in divisores:
    suma=suma + divisor
  if suma == 1:
    primo=True
    return suma,primo
  else:
    primo=False
    return suma,primo