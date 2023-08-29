# completa el código de la función
def amigos(a,b):
  sumaa=0
  sumab=0
  for i in range(1,a):
    if a%i==0:
      sumaa+=i
  for i in range(1,b):
    if b%i==0:
      sumab+=i
  if sumaa==b and sumab==a:
    return True
  else:
    return False
           