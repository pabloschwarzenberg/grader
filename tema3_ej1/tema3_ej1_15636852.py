# completa el código de la función
def suma_divisores(a):
  n=1
  y=0
  while n!=a and n<a:
    if a%n==0:
      y+=n
    n+=1
  if a==1:
    y=0
  return y, y==1
           