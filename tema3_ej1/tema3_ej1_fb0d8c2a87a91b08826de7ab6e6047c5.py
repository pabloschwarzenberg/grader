# completa el código de la función
def suma_divisores(a):
  n=1
  suma=0
  while(n<a):
    if(a%n==0):
      suma += n
      n +=1
    if(a%n!=0):
      n += 1
      suma=suma
  while(n==a):
    if(suma==1):
      return (1,True)
    elif(n==1):
      return (0,False)
    else:
      return (suma,False)