# completa el código de la función
def amigos(a,b): 
  if a==b: return False
  sumaa=sum(divisores for divisores in range(1,a) if a%divisores==0)
  sumab=sum(divisores for divisores in range(1,b) if b%divisores==0)
  if (sumaa==b and sumab==a):
    return True
  else:
    return False
           