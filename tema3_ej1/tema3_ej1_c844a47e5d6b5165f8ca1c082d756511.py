# completa el código de la función
def suma_divisores(a):
  b=a
  suma=0
  p=False
  while b>1:
    b-=1
    if a%b==0:
      suma+=b
  if suma==1:
    p=True
    
  return (suma,p)
          