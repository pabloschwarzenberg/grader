# completa el código de la función
def suma_divisores(a):
  sumaDiv = 0
  for i in range(1,a):
    if a%i==0:
      sumaDiv = sumaDiv + i
  if sumaDiv==1:
    x=True
  else:
    x=False
  return(sumaDiv,x)