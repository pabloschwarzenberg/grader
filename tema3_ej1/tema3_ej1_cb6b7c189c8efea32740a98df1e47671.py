# completa el código de la función
def suma_divisores(a):
  n=1
  r=0
  while n<a :
    if a%n == 0 :
      r=r+n
    n=n+1
  if r==1:
    return r,True
  else:
    return r,False