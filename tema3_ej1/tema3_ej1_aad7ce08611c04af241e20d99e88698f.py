# completa el código de la función
def suma_divisores(a):
  suma=0
  divisor=1
  while divisor<a:
    if a%divisor==0:
      suma+=divisor
    divisor+=1
  if suma==1:
    veredicto=True
  else:
    veredicto=False
  return suma, veredicto
           