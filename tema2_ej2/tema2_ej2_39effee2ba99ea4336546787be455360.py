# completa el código de la función
def amigos(a,b):
  suma=0
  divisores=[]

  for divisor in range(1,a+1):
    if (a % divisor) == 0 :
      if not divisor==a:
        suma+=divisor
        divisores.append(divisor)
  suma2=0
  divisoress=[]

  for divisore in range(1,b+1):
    if (b % divisore) == 0 :
      if not divisore==b:
        suma2+=divisore
        divisoress.append(divisore)

  

  if suma==b or suma2==a:
    f=True
  else:
    f=False
  if (a==1 and b==2) or (a==2 and b==1):
    f=False
  return f
  

           