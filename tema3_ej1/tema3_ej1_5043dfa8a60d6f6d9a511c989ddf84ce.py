# completa el código de la función
def suma_divisores(a):
  L=[]
  suma=0
  primo=False
  for i in range(1,a):
    n=a%i
    if n==0:
      L.append(i)
  for j in range(len(L)):
    suma+=L[j]
  if suma==1:
    primo=True
    return suma, primo
  else:
    return suma, primo
           