# completa el código de la función
def suma_divisores(a):
  d=0
  if a<=1:
    return (0,False)
  for i in range(1,a):
    if a%i==0:
      d=d+i
    elif a%i!=0:
      continue
  if d==1:
    return (d,True)
  elif d!=1:
    return (d,False)
      
 
           