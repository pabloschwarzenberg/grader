# completa el código de la función
def suma_divisores(a):
  suma=0
  for i in range(1,a):
    if a%i==0:
      suma+=i
  Primo=True
  if a<=1:
    Primo=False
  elif a==2:
    Primo=True
  else:
    for i in range(2,a):
      if a%i==0:
        Primo=False

  return(suma,Primo)