# completa el código de la función
def amigos(a,b):
  diva=[]
  divb=[]
  suma=0
  sumb=0
  for i in range(a):
    if i==0:
      continue
    if a%i==0:
      diva.append(i)
  for i in range(b):
    if i==0:
      continue
    if b%i==0:
      divb.append(i)
  for i in diva:
    suma+=i
  for i in divb:
    sumb+=i
  if suma==b and sumb==a:
    return True
  else:
    return False