# completa el código de la función
def amigos(a,b):
  suma=0
  suma1=0
  for k in range(1,a):
    if a%k==0:
      suma=suma+k
  if suma==b:
    return True
  else:
    return False
  for q in range(1,b):
    if b%q==0:
      suma1=suma1+q
  if suma1==a:
    return True
  else:
    return False
           