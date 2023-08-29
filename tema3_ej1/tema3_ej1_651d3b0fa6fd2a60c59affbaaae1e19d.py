# completa el código de la función
def suma_divisores(a):
  k=0
  i=1
  while i<a:
    if a%i==0:
      k=i+k
    i=i+1
  if k==1:
    return k,True
  else:
    return k,False
           