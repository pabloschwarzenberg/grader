# completa el código de la función
def suma_divisores(a):
  f=0
  if a==1:
      return (0,False)
  for i in range(1,a):
    if a%i==0:
      f=f+i
  for n in range(2,a):
    if a%n==0:
      return (f,False)
  if a==1:
    return (f,False)
  else:
    return (f,True)