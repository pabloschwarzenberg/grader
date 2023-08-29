# completa el código de la función
def suma_divisores(a):
  i=1
  j=0
  while i<a:
    if a%i==0 :
      j=j+i
    i=i+1
  if j==1:
    return j,True
  else:
    return j,False
           