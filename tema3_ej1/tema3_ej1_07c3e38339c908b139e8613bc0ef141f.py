# completa el código de la función
def suma_divisores(a):
  divisor=1
  sumadivisores=0
  while divisor<a:
    if a%divisor==0:
      sumadivisores= sumadivisores + divisor 
      divisor= divisor +1
    else:
     divisor=divisor+1
  if sumadivisores==1:
    return (sumadivisores, True)
  else:
    return (sumadivisores, False)
           