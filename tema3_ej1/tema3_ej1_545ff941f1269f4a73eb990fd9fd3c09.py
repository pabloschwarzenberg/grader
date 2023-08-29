# completa el código de la función
def suma_divisores(a):
  numeros=[]
  i=1
  while i<a:
    if a%i==0:
      numeros.append(i)
    i+=1
  suma=0
  for j in range(len(numeros)):
    suma+=numeros[j]
  primo=False
  if suma==1:
    primo=True
  else:
    primo=False   
  return suma,primo
           