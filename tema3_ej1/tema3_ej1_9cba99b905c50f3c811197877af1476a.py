# completa el código de la función
def suma_divisores(a):
  divisores=0
  divisor=1
  while divisor<a:
    if a%divisor==0:
      divisores+=divisor
    divisor+=1
  if divisores==1:
      return (divisores,True)
  else:
    return (divisores,False)