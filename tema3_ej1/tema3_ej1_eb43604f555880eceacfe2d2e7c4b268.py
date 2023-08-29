# completa el código de la función
def suma_divisores(a):
  suma=0
  if a==1:
    return(0,False)
  else:  
    for i in range(1,a):
      if a%i==0:
        suma+=i
  if suma==1:
    return (suma,True)
  else:
    return (suma,False)
           