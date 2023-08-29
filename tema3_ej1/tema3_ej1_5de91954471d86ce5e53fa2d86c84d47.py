# completa el código de la función
def suma_divisores(a):
  s=0
  for x in range(1,a):
    if a%x==0:
      s+=x
  if s==1:
    boleano=True
  else:
    boleano=False
  return (s,boleano)
           