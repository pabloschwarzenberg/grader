# completa el código de la función
def suma_divisores(a):
  suma=[]
  for x in range (a):
    if x > 0:
      if a % x == 0:
        suma.append(x)
  if sum(suma)==1:
    f=True
  else:
    f=False
  return (sum(suma),f)