# completa el código de la función
def amigos(a,b):
  divisor1=0
  divisor2=0
  for x in range(1,a):
      if a%x==0:
          divisor1+=x
  for y in range(1,b):
      if b%y==0:
          divisor2+=y
  if divisor1==b and divisor2==a:
      return True
  else:
      return False
  