# completa el código de la función
def suma_divisores(a):
  i=0
  suma=0
  primo=False
  if a==1:
    suma=0
  else:
    for i in range(a-1):
      if a%(i+1)==0:
        suma=suma+(i+1)
    if(suma==1):
        primo=True
  return suma,primo
