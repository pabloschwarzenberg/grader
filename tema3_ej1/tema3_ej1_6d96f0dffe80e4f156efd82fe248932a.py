# completa el código de la función
def suma_divisores(a):
  primo=True
  for i in range(0,a):
    if i==0:
      i=1
      total=0
    else:
      if a%i==0:
        total=total+i
  if a<=1:
    primo=False
  elif a==2:
    primo=True
  else:
    for n in range(2,a):
      if a%n==0:
        primo=False
  return total, primo
           