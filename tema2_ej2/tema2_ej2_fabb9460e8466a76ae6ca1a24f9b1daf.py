# completa el código de la función
def amigos(a,b): 
  for i in range(0,a):
    if i==0:
      i=1
      total1=0
    else:
      if a%i==0:
        total1=total1+i
  for i in range(0,b):
    if i==0:
      i=1
      total2=0
    else:
      if b%i==0:
        total2=total2+i
  if total1==b and total2==a:
    return True
  else:
    return False
           