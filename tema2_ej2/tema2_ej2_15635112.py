# completa el código de la función
def amigos(a,b):
  n1=0
  for i in range(1,a):
    if a%i==0:
      n1=n1+i
    else:
      n1=n1
  n2=0
  for i in range(1,b):
    if b%i==0:
      n2=n2+i
    else:
      n2=n2
  if n1==b and n2==a:
    return True
  else:
    return False