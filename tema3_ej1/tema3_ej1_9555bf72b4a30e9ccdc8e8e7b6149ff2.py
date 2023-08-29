# completa el código de la función
def suma_divisores(a):
  sd=0
  primo=False
  if a<2:
    return sd,primo
  for i in range(1,a):
    if a%i==0:
      sd+=i
  if sd==1:
    primo=True
  return sd,primo
           