# completa el código de la función
def suma_divisores(a):
  if a==1:
    return (0,False)
  suma=0
  for i in range(1,a):
    if a%i==0:
      suma=suma+i
  if suma==1:
    return (1,True)
  else:
    return (suma,False)    
