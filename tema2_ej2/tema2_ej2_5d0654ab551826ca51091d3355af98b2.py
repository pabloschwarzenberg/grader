# completa el código de la función
def amigos(a,b):
  if a==b: return False
  suma=sum(i for i in range(1,a)if a%i==0)
  sumb=sum(i for i in range(1,b)if b%i==0)
  if suma==b and sumb==a:
    return True
  else:
    return False
           