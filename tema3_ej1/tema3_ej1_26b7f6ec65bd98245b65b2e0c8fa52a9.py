# completa el código de la función
def suma_divisores(a):
  divisores=[]
  divisor=1
  while divisor<a:
    if a%divisor==0:
      divisores.append(divisor)
    divisor=divisor+1
  i=0
  suma=0
  for i in divisores:
    suma=i+suma
    print(suma)
    i=i+1
  
  if len(divisores)>1:
    return (suma,False)
  elif len(divisores)==1:
    return (suma,True)
  elif len(divisores)==0:
    return (suma,False)
